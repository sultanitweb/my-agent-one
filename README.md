# my-agent-one
Temporary Fix (for the current terminal session)
This is the fastest way to get your script running. The environment variable will only be set for the duration of the current terminal session. If you close the terminal or open a new one, you'll have to set it again.

Open your terminal.

Set the environment variable.


export GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Note: Replace YOUR_API_KEY_HERE with your actual Gemini API key. Make sure there are no spaces around the equals sign (=).



The output "Hello! I am doing well, thank you for asking. How are you today?" confirms that:

Your main.py script was able to import the config object from connection.py.

The GOOGLE_API_KEY environment variable was correctly set and read by your script.

The AsyncOpenAI client successfully connected to the Gemini API endpoint.

The agent received the prompt "Hello, how are you." and generated a coherent response.

This is a great first step. Now that your basic setup is functional, you can start building more complex interactions, giving your agent new instructions, or integrating tools to make it more powerful.
