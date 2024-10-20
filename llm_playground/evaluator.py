import time

class Evaluator:
    def __init__(self, claude_api):
        self.claude_api = claude_api

    def evaluate_prompt(self, prompt, num_runs=1):
        results = []
        for _ in range(num_runs):
            start_time = time.time()
            response = self.claude_api.generate_response(prompt)
            end_time = time.time()
            
            if response:
                results.append({
                    "response": response["completion"],
                    "time_taken": end_time - start_time,
                    "input_tokens": response["input_tokens"],
                    "output_tokens": response["output_tokens"],
                    "total_tokens": response["total_tokens"]
                })
            else:
                results.append({
                    "response": None,
                    "time_taken": end_time - start_time,
                    "input_tokens": None,
                    "output_tokens": None,
                    "total_tokens": None
                })
        
        return results

    def calculate_metrics(self, results):
        total_time = sum(result["time_taken"] for result in results)
        avg_time = total_time / len(results)
        
        total_input_tokens = sum(result["input_tokens"] for result in results if result["input_tokens"] is not None)
        total_output_tokens = sum(result["output_tokens"] for result in results if result["output_tokens"] is not None)
        total_tokens = sum(result["total_tokens"] for result in results if result["total_tokens"] is not None)
        
        return {
            "total_time": total_time,
            "average_time": avg_time,
            "num_runs": len(results),
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_tokens": total_tokens,
            "average_input_tokens": total_input_tokens / len(results) if len(results) > 0 else 0,
            "average_output_tokens": total_output_tokens / len(results) if len(results) > 0 else 0,
            "average_total_tokens": total_tokens / len(results) if len(results) > 0 else 0
        }
