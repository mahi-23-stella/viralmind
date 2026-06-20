from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "ViralMind Backend Running"


def generate_reel_ideas(niche):

    ideas = {
        "fashion": [
            "3 Outfit Mistakes Killing Your Style",
            "Zara vs H&M Styling Challenge",
            "One Dress, 5 Different Looks"
        ],

        "fitness": [
            "Why Your Fat Loss Isn't Working",
            "30 Day Transformation Plan",
            "Gym Mistakes Beginners Make"
        ],

        "tech": [
            "Top AI Tools This Month",
            "Hidden Phone Features",
            "Best Productivity Apps"
        ],

        "business": [
            "Side Hustles That Actually Work",
            "Passive Income Myths",
            "Business Lessons From Startups"
        ],

        "travel": [
            "Hidden Places Nobody Knows",
            "Budget Travel Hacks",
            "Weekend Trip Ideas"
        ],

        "lifestyle": [
            "My Productive Morning Routine",
            "Habits That Changed My Life",
            "Things I Stopped Doing"
        ]
    }

    return ideas.get(niche.lower(), ideas["lifestyle"])


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.json

    username = data.get("username", "creator")
    niche = data.get("niche", "lifestyle")

    ideas = generate_reel_ideas(niche)

    result = {

        "viralScore": random.randint(78, 95),

        "stats": {
            "avgViews": f"{random.randint(50,300)}K",
            "engagementRate": f"{round(random.uniform(4.5,11.5),1)}%"
        },

        "trendingTopics": [
            f"{niche.title()} Tips",
            f"{niche.title()} Hacks",
            f"{niche.title()} Trends 2026",
            "Storytelling Content",
            "Personal Branding"
        ],

        "contentGaps": [
            "Educational content missing",
            "Low storytelling content",
            "No challenge-based reels",
            "No audience interaction posts"
        ],

        "growthRecommendations": [
            "Post 4-5 reels per week",
            "Use stronger hooks in first 3 seconds",
            "Add captions to every reel",
            "Reply to comments within 1 hour",
            "Collaborate with creators in your niche"
        ],

        "audienceInsights": [
            "Audience prefers short-form videos",
            "Tutorial content performs best",
            "Motivational content gets more shares",
            "Before/After content has strong engagement"
        ],

        "hashtags": {

            "mega": [
                "#viral",
                "#fyp",
                "#explorepage"
            ],

            "trending": [
                "#reels",
                "#trending",
                "#growth"
            ],

            "niche": [
                f"#{niche}",
                f"#{niche}tips",
                f"#{niche}creator"
            ]
        },

        "bestTimes": {
            "Mon": ["7PM"],
            "Tue": ["8PM"],
            "Wed": ["7PM"],
            "Thu": ["8PM"],
            "Fri": ["6PM"],
            "Sat": ["12PM"],
            "Sun": ["10AM"]
        },

        "calendar": [
            {
                "day": "Mon",
                "time": "7PM",
                "content": "Educational Reel"
            },
            {
                "day": "Tue",
                "time": "8PM",
                "content": "Trending Reel"
            },
            {
                "day": "Wed",
                "time": "7PM",
                "content": "Storytelling Reel"
            },
            {
                "day": "Thu",
                "time": "8PM",
                "content": "Tutorial Reel"
            },
            {
                "day": "Fri",
                "time": "6PM",
                "content": "Audience Q&A"
            },
            {
                "day": "Sat",
                "time": "12PM",
                "content": "Behind The Scenes"
            },
            {
                "day": "Sun",
                "time": "10AM",
                "content": "Weekly Recap"
            }
        ],

        "reelIdeas": [

            {
                "rank": 1,
                "trendType": "hot",
                "topic": ideas[0],
                "description": "High viral potential topic",
                "hooks": [
                    "Stop scrolling...",
                    "Nobody talks about this"
                ],
                "format": "Reel",
                "duration": "30s",
                "virality": "95%"
            },

            {
                "rank": 2,
                "trendType": "rising",
                "topic": ideas[1],
                "description": "Growing audience interest",
                "hooks": [
                    "You need to see this",
                    "Most people do this wrong"
                ],
                "format": "Reel",
                "duration": "45s",
                "virality": "89%"
            },

            {
                "rank": 3,
                "trendType": "evergreen",
                "topic": ideas[2],
                "description": "Long-term content opportunity",
                "hooks": [
                    "Save this for later",
                    "Here's the truth"
                ],
                "format": "Carousel",
                "duration": "60s",
                "virality": "83%"
            }
        ],

        "profile": {
            "username": username,
            "niche": niche
        }
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000)