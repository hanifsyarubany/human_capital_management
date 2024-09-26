from prompt_template import *
from setup import *
import random
import threading
from fastapi import FastAPI
import uvicorn
import gradio as gr

""" GENERATE COMPLETION """
def generate_completion(system_prompt,user_prompt,token=256):
   response = client.chat.completions.create(
   model="gpt-4o",
   messages=[
      {
         "role": "system",
         "content": [
         {
            "type": "text",
            "text": system_prompt
         }
         ]
      },
      {
         "role": "assistant",
         "content": [
         {
            "type": "text",
            "text": user_prompt
         }
         ]
      },
   ],
   temperature=0,
   max_tokens=token,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
   )
   return (response.choices[0].message.content)

""" MAIN FAST API """
app = FastAPI()
@app.get("/post-retrieve-all-outputs")
def retrieve_all_outputs(session_id): 
    global unique_code
    dict_all_combines = {}
    def generating_output(cv_content,jobdesc,role,index):
        # GENERATING PROS
        pros_result = generate_completion(system_prompt_pros,PromptReplacer(user_prompt_main).replace_entities({
            "<<cv_text>>":cv_content,
            "<<jobdesc>>":jobdesc,
            "<<role>>":role
            }))
        arr_pros = pros_result.split("===")
        dict_pros = {
            "1":arr_pros[0],
            "2":arr_pros[1],
            "3":arr_pros[2]
        }

        # GENERATING CONS
        cons_result = generate_completion(system_prompt_cons,PromptReplacer(user_prompt_main).replace_entities({
            "<<cv_text>>":cv_content,
            "<<jobdesc>>":jobdesc,
            "<<role>>":role
        }))
        arr_cons = cons_result.split("===")
        dict_cons = {
            "1":arr_cons[0],
            "2":arr_cons[1],
            "3":arr_cons[2]
        }

        # GENERATING OTHER DETAILS
        red_flags_result = generate_completion(system_prompt_red_flags,PromptReplacer(user_prompt_main).replace_entities({
            "<<cv_text>>":cv_content,
            "<<jobdesc>>":jobdesc,
            "<<role>>":role
        }))
        cultural_skills_result = generate_completion(system_prompt_cultural_softskills,PromptReplacer(user_prompt_main).replace_entities({
            "<<cv_text>>":cv_content,
            "<<jobdesc>>":jobdesc,
            "<<role>>":role
            }))
        long_term_result = generate_completion(system_prompt_longterm_potential,PromptReplacer(user_prompt_main).replace_entities({
            "<<cv_text>>":cv_content,
            "<<jobdesc>>":jobdesc,
            "<<role>>":role
            }))
        
        # GENERATING DICT OUTPUT
        dict_output = {
            "role": role,
            "job_description":jobdesc,
            "pros_analysis": dict_pros,
            "cons_analysis": dict_cons,
            "red_flags_indication":red_flags_result,
            "cultural_fit_and_soft_skills_insights":cultural_skills_result,
            "long_term_potential":long_term_result
        }

        # RETURN OUTPUT
        dict_all_combines[f"job_matching_{index}"] = dict_output


    # Defince CV Content
    cv_content = [i for i in collection_cvinput.find({"session_id":session_id})][-1]["content"]
    # Define arr_jobs
    arr_jobs = [i for i in collection_jobdesc.find({"unique_code":unique_code})]
    # Randomly pick 5 elements from the array
    random_elements = random.sample([i for i in range(len(arr_jobs))], 5)

    # Define Threads
    t1 = threading.Thread(target=generating_output, args=(cv_content,arr_jobs[random_elements[0]]["jobdesc"],arr_jobs[random_elements[0]]["role"],1))
    t2 = threading.Thread(target=generating_output, args=(cv_content,arr_jobs[random_elements[1]]["jobdesc"],arr_jobs[random_elements[1]]["role"],2))
    t3 = threading.Thread(target=generating_output, args=(cv_content,arr_jobs[random_elements[2]]["jobdesc"],arr_jobs[random_elements[2]]["role"],3))
    t4 = threading.Thread(target=generating_output, args=(cv_content,arr_jobs[random_elements[3]]["jobdesc"],arr_jobs[random_elements[3]]["role"],4))
    t5 = threading.Thread(target=generating_output, args=(cv_content,arr_jobs[random_elements[4]]["jobdesc"],arr_jobs[random_elements[4]]["role"],5))

    # Starting thread
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # Joining thread
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    # Return Output
    return dict_all_combines