from requests import post


def send_alert(message: str):
    slack_webhook_url = "https://hooks.slack.com/triggers/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"
    if slack_webhook_url == 'None':
        return
    post(slack_webhook_url, json={"title": ":windows95: ec2 cron :windows95:", "message": message})
