
from agents import Agent, Runner
import dotenv

# Load the environment variables
dotenv.load_dotenv()

def main():
    agent = Agent(name="well_test_assistant", instructions="You are well test assistant. You are responsible for checking well tests and validating the results by checking against the historic values.")

    result = Runner.run_sync(agent, "well test 1")
    print(result.final_output)



if __name__ == "__main__":
    main()
