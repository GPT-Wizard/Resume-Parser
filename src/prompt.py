def basic_prompt_template(context, user_input):
    return f"""Here is the candidate's resume:
    {context}
    Here is the query:
    {user_input}
    """

def summary_prompt_template(context):
    return f"""Here is the candidate's resume:
    {context}
    Create a short summary of the candidate's profile with key points.
    Summary in markdown format:
    """