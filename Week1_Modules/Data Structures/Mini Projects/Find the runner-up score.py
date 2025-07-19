# Runner-up Score Finder
# University Sports Day Score Sheet

def find_runner_up_score(scores):
    """Find the runner-up (second highest) score from a list"""

    unique_scores = sorted(set(scores), reverse=True)
    
 
    if len(unique_scores) >= 2:
        return unique_scores[1]
    else:
        return "Not enough unique scores"

scores = [2, 3, 6, 6, 5]
runner_up = find_runner_up_score(scores)

print(f"Sample input: {scores}")
print(f"Sample output: {runner_up}")

print(f"\nExplanation: Given list is {scores}. The maximum score is {max(scores)}, second maximum is {runner_up}. Hence, we print {runner_up} as the runner-up score.")


print("\n" + "="*50)
print("RUNNER-UP SCORE FINDER")
print("="*50)

while True:
    try:
        user_input = input("\nEnter scores separated by spaces (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
            
        user_scores = list(map(int, user_input.split()))
        
        if len(user_scores) < 2:
            print("Please enter at least 2 scores!")
            continue
            
        runner_up = find_runner_up_score(user_scores)
        max_score = max(user_scores)
        
        print(f"Scores: {user_scores}")
        print(f"Runner-up score: {runner_up}")
        print(f"Explanation: Maximum score is {max_score}, second maximum is {runner_up}")
        
    except ValueError:
        print("Please enter valid numbers separated by spaces!")
    except Exception as e:
        print(f"Error: {e}")

print("Thanks for using the Runner-up Score Finder!")