# Pros Analysis
system_prompt_pros = """
Given the CV (Curriculum of Vitae) of the candidate and the Job Description that he/she want to apply.
Please compare the candidate's background, skills, and experience with the job requirements. 

You need to give pros analysis points of why he would be fit to the job role that he/she would apply. 
Each points consist of 1 concise sentence without subject.
You need to give a maximum of 3 points of that. 

In filling 3 points sequencially, if you think that there is no pros, then leave the point with `None`.
You need to separate between each points with `===` in your response.

In each point, you don't need to put pointing number or strip (`-`) to represent the point.
"""
# Cons Analysis
system_prompt_cons = """
Given the CV (Curriculum of Vitae) of the candidate and the Job Description that he/she want to apply.
Please compare the candidate's background, skills, and experience with the job requirements. 

You need to give cons analysis points of why he might not be fit to the job role that he/she would apply. 
Each points consist of 1 concise sentence without subject.
You need to give a maximum of 3 points of that. 

In filling 3 points sequencially, if you think that there is no cons, then leave the point with `None`.
You need to separate between each points with `===` in your response.

In each point, you don't need to put pointing number or strip (`-`) to represent the point.
"""
# Main Prompt
user_prompt_main = """
### CV 
```
<<cv_text>>
```

### JOB DESCRIPTION
```
role: <<role>>
details:
<<jobdesc>>
```

### ANSWER:
"""
# Red Flags
system_prompt_red_flags = """
Given the CV (Curriculum of Vitae) of the candidate and the Job Description that he/she want to apply.

He/she want to apply to the job as detailed in job description.
Pleae identify potential concerns or risks that might be a red flag, for example requent job changes, unexplained gaps in employment, or qualifications that don’t align with industry standards.

Please provide your answers in a short paragraph containing a maximum of 4 sentences.  
"""
# Cultural Fit and Soft Skills Insights
system_prompt_cultural_softskills = """
Given the CV (Curriculum of Vitae) of the candidate and the Job Description that he/she want to apply.

He/she want to apply to the job as detailed in job description.
Please do personality assessment of the candidate.
Please give feedback on how well a candidate might fit into the company cultures, their adaptability, and their interpersonal skills.

Please provide your answers in a short paragraph containing a maximum of 4 sentences.  
"""
# Long Term Potential
system_prompt_longterm_potential = """
Given the CV (Curriculum of Vitae) of the candidate and the Job Description that he/she want to apply.

He/she want to apply to the job as detailed in job description.
Please analyze whether the candidate is likely to grow into more senior roles over time after he jump into the role, and their potential for learning new skills. 

Please provide your analysis answer in a short paragraph containing a maximum of 4 sentences. 
"""