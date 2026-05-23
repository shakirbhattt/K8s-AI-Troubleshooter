import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ai_diagnose(issues):

    if not issues:
        return """
Cluster analysis completed successfully.

No critical issues detected.
Recommendations:
- Continue monitoring
- Ensure alerts are configured
- Regularly review pod health
"""

    prompt = f"""
You are a senior Kubernetes Site Reliability Engineer.

Analyze the following Kubernetes pod issues:

{issues}

Provide:
1. Root Cause
2. Impact
3. Recommended Fix
4. Best Practices

Keep response concise and technical.
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Analysis Error: {str(e)}"
