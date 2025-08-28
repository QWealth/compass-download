from requests import post


def send_alert(message: str):
    slack_webhook_url = "https://hooks.slack.com/triggers/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"
    if slack_webhook_url == 'None':
        return
    post(slack_webhook_url, json={"title": ":windows95: ec2 cron :windows95:", "message": message})
