# AI Digital Learning Assistant with OpenAI API

Welcome to the AI Digital Learning Assistant! This tool is your one-stop solution for personalized study plans, dynamic content generation, and comprehensive decision support, all powered by the OpenAI API. Seamlessly integrated with Rasa, a popular open-source chatbot framework, this assistant offers a powerful way to enhance your learning experience and decision-making process.

## Key Features

- **Personalized Study Plans:** Craft effective study plans tailored to your specific goals using the power of GPT-3.5-turbo.
- **Dynamic Content Generation:** Access high-quality, relevant content dynamically generated based on your needs.
- **Comprehensive Decision Support:** Make informed choices with clear and concise analyses of pros and cons presented by your AI assistant.

## Getting Started

### Prerequisites
Ensure you have Rasa installed and configured. Refer to the [official Rasa documentation](https://rasa.com/docs/) for detailed setup instructions.

### Running the Assistant
To run the actions defined in `actions.py`:
```bash
rasa run actions --actions actions
```
To enable the API and run the trained models:
```bash
rasa run -m models --enable-api --cors "*" --debug
```

### API Integration
Replace `YOUR_OPENAI_API_KEY` with your actual OpenAI API key in the code to enable integration with the OpenAI API.

```python
headers = {
    'Authorization': 'Bearer YOUR_OPENAI_API_KEY',
    'Content-Type': 'application/json'
}
```

## Understanding the Code

### ActionDefaultFallback

Acts as a safety net, handling situations where the user's intent is not recognized.

#### ActionStudyPlan

Retrieves the user's message, constructs a request to the OpenAI API's chat/completions endpoint, processes the response, and delivers the study plan.

#### ActionDynamicContent

Generates dynamic content based on user requests.

#### ActionDecisionSupport

Provides comprehensive decision support by analyzing pros and cons.

## See the AI Digital Learning Assistant in Action!

[Click here to watch a video demo](https://drive.google.com/file/d/1AZM0n6Y2QOzdYWdpDqSHIJB9MuN9pLuy/view?usp=drive_link)

## Additional Notes

- Explore the Rasa documentation for further customization and development options: [Rasa Documentation](https://rasa.com/docs/)
- Consider security best practices when storing and using your OpenAI API key.

## Get Started Today!

This readme equips you with the foundational knowledge to leverage the AI Digital Learning Assistant. With its capabilities and your ingenuity, unlock a world of personalized learning and informed decision-making. Feel free to explore, customize, and make this assistant your own!
