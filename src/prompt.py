def qa_prompt_template(context, user_input):
    return f"""
    {context}
    {user_input}
    """

def summary_prompt_template(context):
    return f"""Here is the candidate's resume:
    {context}
    Create a short summary of the candidate's profile with key points.
    Summary in markdown format:
    """