from typing import Dict, List, Optional, Tuple
import re

class InterviewLogicHandler:
    def __init__(self, conversation_flows: List[Dict]):
        self.conversation_flows = conversation_flows

    def detect_triggers(self, topic: str, response: str, evaluation: Dict) -> List[Dict]:
        """
        Detect which triggers are present in the response and evaluation
        Returns list of matching follow-up questions
        """
        # Find the conversation flow for the current topic
        topic_flow = next(
            (flow for flow in self.conversation_flows 
             if flow["initial_topic"] == topic),
            None
        )
        
        if not topic_flow:
            return []

        matched_triggers = []
        for follow_up in topic_flow["follow_up_questions"]:
            trigger = follow_up["trigger"].lower()
            # Check in response text
            if trigger in response.lower():
                matched_triggers.append(follow_up)
            # Check in evaluation comments
            if trigger in evaluation["technical_accuracy"]["comments"].lower():
                matched_triggers.append(follow_up)
            if trigger in evaluation["understanding_depth"]["comments"].lower():
                matched_triggers.append(follow_up)

        return matched_triggers

    def select_next_question(
        self, 
        topic: str, 
        response: str, 
        evaluation: Dict,
        current_question_level: str = "base"
    ) -> Tuple[str, str, List[str]]:
        """
        Select the next question based on response evaluation
        Returns: (question_type, question_text, deeper_questions)
        """
        # If we're at base question, look for triggers
        if current_question_level == "base":
            matched_triggers = self.detect_triggers(topic, response, evaluation)
            if matched_triggers:
                # Select the first matched trigger's question
                return (
                    "follow_up",
                    matched_triggers[0]["question"],
                    matched_triggers[0]["deeper_questions"]
                )

        # If we're at follow-up and score is good, move to deeper questions
        elif current_question_level == "follow_up":
            technical_score = evaluation["technical_accuracy"]["score"]
            if technical_score >= 85:  # Threshold for moving to deeper questions
                topic_flow = next(
                    (flow for flow in self.conversation_flows 
                     if flow["initial_topic"] == topic),
                    None
                )
                if topic_flow:
                    current_trigger = self.detect_triggers(topic, response, evaluation)[0]
                    return (
                        "deeper",
                        current_trigger["deeper_questions"][0],
                        current_trigger["deeper_questions"][1:]
                    )

        # Check exit conditions
        if self.should_exit_topic(topic, evaluation):
            return ("exit", "Move to next topic", [])

        return ("continue", "Continue with current question", [])

    def should_exit_topic(self, topic: str, evaluation: Dict) -> bool:
        """
        Check if we should exit the current topic based on evaluation
        """
        topic_flow = next(
            (flow for flow in self.conversation_flows 
             if flow["initial_topic"] == topic),
            None
        )
        
        if not topic_flow:
            return True

        for exit_condition in topic_flow["exit_conditions"]:
            # Check if any exit condition appears in the evaluation
            if (
                exit_condition.lower() in evaluation["overall_feedback"].lower() or
                evaluation["technical_accuracy"]["score"] < 70
            ):
                return True

        return False 