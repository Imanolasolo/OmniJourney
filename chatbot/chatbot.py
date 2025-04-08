import openai
from database.database import insert_interaction

def chat_with_bot(api_key, user_input, chatbot_id=None, knowledge_base=None):
    openai.api_key = api_key

    # Construir el prompt con la base de conocimiento (si existe)
    prompt = ""
    if knowledge_base:
        prompt += f"Base de conocimiento:\n{knowledge_base}\n\n"
    prompt += f"Pregunta del usuario: {user_input}\nRespuesta del chatbot:"

    # Llamar a la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    bot_response = response.choices[0].text.strip()

    # Registrar la interacción en la base de datos
    if chatbot_id:
        insert_interaction(chatbot_id, user_input, bot_response)

    return bot_response