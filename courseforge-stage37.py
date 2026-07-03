# === Stage 37: Add recommendations for the next useful action ===
# Project: CourseForge
from typing import Optional, List
import random
from datetime import datetime, timedelta

def generate_smart_recommendations(user_progress: dict) -> List[str]:
    """
    Generates a list of actionable recommendations based on user progress data.
    Prioritizes weak areas and upcoming deadlines while suggesting review tasks.
    
    Args:
        user_progress (dict): Contains 'completed_modules', 'pending_exercises', 
                              'weak_topics' (list), and 'next_deadline'.
                              
    Returns:
        List[str]: Ordered list of recommendation strings.
    """
    recommendations = []
    
    # 1. Immediate action for weak topics if any exist
    if user_progress.get('weak_topics'):
        topic = random.choice(user_progress['weak_topics'])
        recommendations.append(f"Review concepts in '{topic}' to strengthen your foundation before proceeding.")
        
    # 2. Suggest completing pending exercises, prioritizing those with high difficulty or low score
    pending_exercises = user_progress.get('pending_exercises', [])
    if pending_exercises:
        # Sort by estimated effort (mocked as index for demo) to show variety
        pending_exercises.sort(key=lambda x: x.get('estimated_effort', 1))
        next_task = pending_exercises[0]
        recommendations.append(f"Start working on the exercise: '{next_task['title']}' ({next_task['type']}).")
        
    # 3. Suggest a break or review if progress is high and no immediate tasks
    completed_count = len(user_progress.get('completed_modules', []))
    total_modules = user_progress.get('total_modules', 10)
    
    if completed_count > total_modules * 0.7 and not pending_exercises:
        recommendations.append("You are ahead of schedule! Take a short break or explore advanced documentation.")
        
    # 4. Deadline reminder logic (mocked check)
    next_deadline = user_progress.get('next_deadline')
    if next_deadline:
        days_left = (next_deadline - datetime.now()).days
        if days_left <= 3 and not pending_exercises:
            recommendations.append(f"A deadline is approaching in {days_left} days. Ensure all modules are submitted.")
            
    # 5. General encouragement or resource suggestion
    if not recommendations:
        recommendations.append("Keep up the great work! Consider revisiting earlier lessons for mastery.")
        
    return recommendations
