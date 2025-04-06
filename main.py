
from agents import Agent, Runner, FunctionTool, function_tool
from dotenv import load_dotenv
from pydantic import BaseModel
import pandas as pd


# Load the environment variables
load_dotenv()

df = pd.read_csv("data/well-test-data.csv")


#Define the input schema
class WellTestInput(BaseModel):
    well_id: str
    oil_rate_change: float
    liquid_rate_change: float
    water_cut_change: float
    gas_oil_ratio_change: float
    bhp_change: float


#Defining tools
@function_tool
def get_well_test_data(well_name: str, well_test_model : WellTestInput) -> WellTestInput:
    """
        Get well test data for a specific well.
        Args:
            well_name (str): The name of the well.
            well_test_model (WellTestInput): The well test data model.
        Returns:   
            WellTestInput: The well test data for the specified well.
    """
    # Simulate fetching data from a database or API

    return well_test_model


def main(well_name: str = "DD-07", df: pd.DataFrame = df) -> str:
    df = df[df['wellname'] == well_name][["oil_rate_change","liquid_rate_change","water_cut_change","gas_oil_ratio_change", "bhp_change" 
                                     ,"vrr_change"]]
    print(df)
    
    well_test_model = WellTestInput(
        well_id=well_name,
        oil_rate_change=df.iloc[1,0],
        liquid_rate_change=df.iloc[1,1],
        water_cut_change=df.iloc[1,2],
        gas_oil_ratio_change=df.iloc[1,3],
        bhp_change=df.iloc[1,4]
    )

    #Defining an agent
    agent = Agent(
            name="well_test_assistant", 
            instructions=f'You are well test assistant for well {well_name}. here are the well test data {well_test_model}. You are responsible for checking well tests changes and allerting of significant deviations. The values are indicating percentage changes negative or positive. anything above or below 5 percent should be highlighted.',
            tools=[get_well_test_data],
            )
 
    result = Runner.run_sync(agent, "latest well test data of DD-07 well")
    print(result.final_output)
    print(well_test_model.oil_rate_change)



if __name__ == "__main__":
    main() #run the async function
    #print(df.iloc[:,9:].describe())
