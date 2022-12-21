import requests
import json
import pandas as pd
import matplotlib.pyplot as plot

class hospital_data_analysis:
    def __init__(self, json_link):
        self.json_link=json_link


    def response(self):
        response_API=requests.get(self.json_link)
        data=response_API.json()
        return data
        



     #presents the data in JSON format
newdata=hospital_data_analysis('https://health.data.ny.gov/resource/4ny4-j5zv.json')

abdata=newdata.response()
df = pd.read_json(json.dumps(abdata)) #converts the data to python dataframe for analysis

df2 = df[['age_group','apr_drg_description']].copy() 

visual=df2['age_group'].value_counts(ascending=True)

visual.plot.bar(x="age_group",  rot=0, title="Number of patients per age group")

plot.show(block=True)

most_appearing=df2.age_group.mode() 

new_df=df2[df2['age_group']==str(most_appearing.to_string(index=False))]  #creates a new dataframe consisting of only the agegroup obtained from previous variable(most appearing)

newvisual=new_df['apr_drg_description'].value_counts(ascending=True)



newvisual.plot.bar(x="apr_drg_description",  rot=0, title="Number of patients per illness in the age group")

plot.show(block=True)

most_appearing_disease=new_df.apr_drg_description.mode() #finds the most appearing(mode) disease from the new dataframe 

print('The age group which is most exposed is',most_appearing.to_string(index=False), "and it is mostly exposed to",most_appearing_disease.to_string(index=False)) #prints the output


print('\n') # a new line for easy output reading

regions= df[['hospital_county','ccsr_diagnosis_description']].copy() 


regionvisual=regions['hospital_county'].value_counts(ascending=True)



regionvisual.plot.bar(x="hospital_county",  rot=0, title="Number of patients per region")

plot.show(block=True)

#creates a new dataframe called regions and copulates it by copying columns containing hospital_county and ccsr_diagnosis_description as header

most_affected_region=regions.hospital_county.mode()   #finds the most affected region by calculating the mode of the hospitals county column

most_affecting=regions[regions['hospital_county']==str(most_affected_region.to_string(index=False))] #creates a new dataframe containing of only rows from the most affected region 

illnessvisual=most_affecting['ccsr_diagnosis_description'].value_counts(ascending=True)

illnessvisual.plot.bar(x="ccsr_diagnosis_description",  rot=0, title="Number of patients per infection in the region")

plot.show(block=True)

most_appearing_illness=most_affecting.ccsr_diagnosis_description.mode() #finds the most appearing illness from the nw dataframe to determine the illness which is most affecting the region

print('The region which is most affected is',most_affected_region.to_string(index=False), "and it is mostly affected by",most_appearing_illness.to_string(index=False)) #prints the output


print('\n') #creates a new line

duration= df[['length_of_stay','ccsr_diagnosis_description', 'ccsr_diagnosis_code']].copy() # creates a new dataframe and populates it with data from length_of_stay','ccsr_diagnosis_description' and 'ccsr_diagnosis_code' columns

very_sorted = duration.drop_duplicates(subset=['ccsr_diagnosis_code'],keep='first') #sorts the array by removing entire rows of duplicate values  based on the ccsr_diagnosis_code column

for ind in very_sorted.index: #creates a for loop to iterate between rows in the array
    print('The drug ',df['ccsr_diagnosis_code'][ind], 'cures the disease', df['ccsr_diagnosis_description'][ind], 'in',df['length_of_stay'][ind],'days') #prints output based on each row
    
