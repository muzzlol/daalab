# Define a Job class to store job details
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to perform Job Scheduling to maximize profit
def job_scheduling(jobs, max_deadline):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Initialize result array to keep track of free time slots
    result = [-1] * max_deadline
    # To keep track of scheduled jobs
    scheduled_jobs = []

    # Iterate through each job
    for job in jobs:
        # Find a free slot for this job (from its deadline to earlier slots)
        for slot in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if result[slot] == -1:  # If the slot is free
                result[slot] = job.job_id  # Assign job to the slot
                scheduled_jobs.append(job)  # Add job to the scheduled jobs
                break

    # Return the scheduled jobs and their total profit
    total_profit = sum(job.profit for job in scheduled_jobs)
    return scheduled_jobs, total_profit

# List of jobs with (job_id, deadline, profit)
jobs = [Job('J1', 2, 100), Job('J2', 1, 19), Job('J3', 2, 27), Job('J4', 1, 25), Job('J5', 3, 15)]

# Maximum deadline across all jobs
max_deadline = max(job.deadline for job in jobs)

# Execute job scheduling
scheduled_jobs, total_profit = job_scheduling(jobs, max_deadline)

# Output the result
print("Scheduled Jobs:", [(job.job_id, job.profit) for job in scheduled_jobs])
print("Total Profit:", total_profit)