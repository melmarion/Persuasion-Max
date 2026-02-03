# DEVELOPER QUICKSTART: Build These Tools
## Step-by-Step Implementation Guide

---

## BEFORE YOU START

**You need:**
- Research foundation (read FRACTIONATION_BEHAVIORAL_SCIENCE.md)
- Understanding of why these tools matter (read 00_CORE_THESIS.md)
- API specifications (read 02_TOOL_SPECIFICATIONS.md)

**Time estimate:**
- MVP (1 tool): 2-3 weeks
- 3 tools: 6-8 weeks
- All 12 tools: 6-12 months

---

## PRIORITY: Build in This Order

### Phase 1: MVP (Weeks 1-3)
**Goal: Prove concept, generate research data**

1. **Fractionation Detection Algorithm** (Week 1)
   - Why first: Enables feed analysis for all other tools
   - Difficulty: Medium
   - Deliverable: Python script + API endpoint

2. **Personal Vulnerability Scanner** (Week 2)
   - Why second: Needed for individual-level research
   - Difficulty: Medium
   - Deliverable: Web form + scoring algorithm

3. **Physiological Measurement Suite** (Week 3)
   - Why third: Integrates other tools' outputs
   - Difficulty: High
   - Deliverable: Data pipeline + dashboard

### Phase 2: Core Tools (Weeks 4-8)
4. Behavioral Response Predictor
5. Intervention Effectiveness Simulator
6. Real-Time Influence Detector

### Phase 3: Enterprise Tools (Weeks 9-12)
7. Organizational Vulnerability Assessment
8. Cross-Domain Data Platform

### Phase 4: Impact Tools (Months 4-6)
9. Research Toolkit
10. Digital Engagement Platform
11. Educational Curriculum

---

## TOOL 1: FRACTIONATION DETECTION ALGORITHM
### Week 1 Implementation

### Step 1: Set Up Project Structure

```bash
# Create project directory
mkdir fractionation-detector
cd fractionation-detector

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Initialize git
git init
echo "venv/" > .gitignore

# Create directory structure
mkdir -p src/classifiers src/detectors src/api tests data

# Create requirements.txt
cat > requirements.txt << EOF
nltk==3.8.1
textblob==0.17.1
pandas==2.0.0
scipy==1.10.0
fastapi==0.95.0
uvicorn==0.21.0
pydantic==1.10.0
python-dotenv==1.0.0
pytest==7.3.0
requests==2.28.2
EOF

# Install dependencies
pip install -r requirements.txt
python -m nltk.downloader punkt vader_lexicon
```

### Step 2: Build Content Classifier

**File: `src/classifiers/content_classifier.py`**

```python
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import re

class FractionationClassifier:
    """Classify content into A/J/R/N categories"""

    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

        # Define keywords for each category
        self.anger_keywords = [
            'attack', 'exposed', 'scandal', 'outrage', 'disgusting',
            'betrayal', 'danger', 'threat', 'destroying', 'failing',
            'injustice', 'unfair', 'angry', 'furious', 'enraged'
        ]

        self.joy_keywords = [
            'beautiful', 'heartwarming', 'inspiring', 'love', 'together',
            'amazing', 'community', 'safe', 'family', 'wonderful',
            'grateful', 'happy', 'blessed', 'wonderful', 'joy'
        ]

        self.relief_keywords = [
            'buy', 'shop', 'limited', 'offer', 'now', 'discover',
            'exclusive', 'solution', 'perfect', 'special', 'sale',
            'deal', 'only', 'order', 'click'
        ]

    def classify(self, content):
        """
        Classify content into A/J/R/N
        Returns: {
            'primary_category': 'A'|'J'|'R'|'N',
            'confidence': 0.0-1.0,
            'scores': {'A': score, 'J': score, 'R': score, 'N': score},
            'sentiment': -1.0 to 1.0
        }
        """

        # Get sentiment
        sentiment_scores = self.sia.polarity_scores(content.lower())
        compound = sentiment_scores['compound']

        # Count keyword matches
        anger_count = sum(1 for kw in self.anger_keywords if kw in content.lower())
        joy_count = sum(1 for kw in self.joy_keywords if kw in content.lower())
        relief_count = sum(1 for kw in self.relief_keywords if kw in content.lower())

        # Calculate category scores (0-1)
        scores = {
            'A': min(1.0, (anger_count / 5) + max(0, -compound * 0.3)),
            'J': min(1.0, (joy_count / 5) + max(0, compound * 0.3)),
            'R': min(1.0, relief_count / 3),
            'N': 0.3  # Default neutral score
        }

        # Normalize
        total = sum(scores.values())
        if total > 0:
            scores = {k: v/total for k, v in scores.items()}

        # Determine primary category
        primary = max(scores.items(), key=lambda x: x[1])

        return {
            'primary_category': primary[0],
            'confidence': primary[1],
            'scores': scores,
            'sentiment': compound
        }
```

### Step 3: Build Sequence Detector

**File: `src/detectors/sequence_detector.py`**

```python
from typing import List, Dict
from scipy.stats import chi2_contingency

class SequenceDetector:
    """Detect fractionation patterns in feed sequences"""

    def __init__(self):
        self.target_pattern = ['A', 'J', 'A', 'R']
        self.window_size = 4

    def detect_patterns(self, classified_feed: List[str]) -> Dict:
        """
        Find A-J-A-R patterns in classified feed
        classified_feed: List of categories ['A', 'J', 'R', 'N', ...]
        """

        patterns = []

        # Sliding window
        for i in range(len(classified_feed) - self.window_size + 1):
            window = classified_feed[i:i + self.window_size]

            if window == self.target_pattern:
                patterns.append({
                    'position': i,
                    'sequence': window,
                    'strength': 0.85  # Would calculate from intensity scores
                })

        # Statistical significance test
        observed_count = len(patterns)

        # Calculate expected count (if random)
        category_counts = {
            'A': classified_feed.count('A'),
            'J': classified_feed.count('J'),
            'R': classified_feed.count('R'),
            'N': classified_feed.count('N')
        }
        total = len(classified_feed)

        probabilities = {k: v/total for k, v in category_counts.items()}
        expected_count = (total - 3) * (
            probabilities['A'] * probabilities['J'] *
            probabilities['A'] * probabilities['R']
        )

        # Chi-square test
        if expected_count > 0:
            chi2 = (observed_count - expected_count) ** 2 / expected_count
            p_value = 1 - chi2  # Simplified; use scipy.stats.chi2.sf in production
        else:
            p_value = 1.0

        return {
            'patterns_found': observed_count,
            'expected_random': expected_count,
            'chi2_statistic': chi2 if expected_count > 0 else 0,
            'p_value': p_value,
            'statistically_significant': p_value < 0.05,
            'patterns': patterns
        }

    def calculate_fractionation_index(self, detected_patterns: Dict) -> float:
        """
        Calculate 0-100 fractionation index
        """
        observed = detected_patterns['patterns_found']
        expected = detected_patterns['expected_random']

        if expected == 0:
            return 0.0

        ratio = observed / expected

        if ratio < 1:
            return 0.0

        # Map ratio to 0-100 score
        # ratio 1 = 0 points (random)
        # ratio 2 = 50 points (2x random)
        # ratio 5+ = 100 points (heavily influenced)

        index = min(100, (ratio - 1) * 50)
        return index
```

### Step 4: Build API Endpoint

**File: `src/api/main.py`**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.classifiers.content_classifier import FractionationClassifier
from src.detectors.sequence_detector import SequenceDetector

app = FastAPI()
classifier = FractionationClassifier()
detector = SequenceDetector()

class FeedItem(BaseModel):
    id: str
    content: str
    timestamp: str

class AnalysisRequest(BaseModel):
    feed_id: str
    items: List[FeedItem]

@app.post("/api/v1/analyze/feed")
async def analyze_feed(request: AnalysisRequest):
    """Analyze feed for fractionation patterns"""

    try:
        # Classify each item
        classifications = []
        for item in request.items:
            result = classifier.classify(item.content)
            classifications.append({
                'item_id': item.id,
                'category': result['primary_category'],
                'confidence': result['confidence']
            })

        # Extract sequence
        sequence = [c['category'] for c in classifications]

        # Detect patterns
        patterns = detector.detect_patterns(sequence)

        # Calculate fractionation index
        fractionation_index = detector.calculate_fractionation_index(patterns)

        return {
            'feed_id': request.feed_id,
            'total_items': len(request.items),
            'classifications': classifications,
            'pattern_analysis': patterns,
            'fractionation_index': fractionation_index,
            'interpretation': f"Fractionation level: {fractionation_index:.0f}/100"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 5: Create Tests

**File: `tests/test_classifier.py`**

```python
import pytest
from src.classifiers.content_classifier import FractionationClassifier

@pytest.fixture
def classifier():
    return FractionationClassifier()

def test_anger_classification(classifier):
    content = "This is an outrage! We must attack the injustice!"
    result = classifier.classify(content)
    assert result['primary_category'] == 'A'
    assert result['confidence'] > 0.5

def test_joy_classification(classifier):
    content = "What a beautiful and heartwarming story of love and family!"
    result = classifier.classify(content)
    assert result['primary_category'] == 'J'
    assert result['confidence'] > 0.5

def test_relief_classification(classifier):
    content = "Buy now! Limited exclusive offer only today. Click here!"
    result = classifier.classify(content)
    assert result['primary_category'] == 'R'
    assert result['confidence'] > 0.3

def test_neutral_classification(classifier):
    content = "Weather today will be cloudy with chance of rain."
    result = classifier.classify(content)
    assert result['primary_category'] == 'N'
```

**File: `tests/test_detector.py`**

```python
import pytest
from src.detectors.sequence_detector import SequenceDetector

@pytest.fixture
def detector():
    return SequenceDetector()

def test_pattern_detection(detector):
    # Feed with fractionation pattern
    sequence = ['N', 'A', 'J', 'A', 'R', 'N', 'A', 'J', 'A', 'R']

    results = detector.detect_patterns(sequence)
    assert results['patterns_found'] > 0
    assert results['statistically_significant'] == True

def test_no_pattern_detection(detector):
    # Random feed
    sequence = ['N', 'N', 'J', 'N', 'R', 'A', 'J', 'N']

    results = detector.detect_patterns(sequence)
    assert results['patterns_found'] == 0

def test_fractionation_index(detector):
    sequence = ['A', 'J', 'A', 'R', 'A', 'J', 'A', 'R']
    results = detector.detect_patterns(sequence)
    index = detector.calculate_fractionation_index(results)

    assert index > 50  # Should show significant fractionation
```

### Step 6: Run Tests

```bash
pytest tests/ -v
pytest tests/test_classifier.py::test_anger_classification -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html
```

### Step 7: Deploy API

```bash
# Start development server
python -m uvicorn src.api.main:app --reload

# Test endpoint
curl -X POST "http://localhost:8000/api/v1/analyze/feed" \
  -H "Content-Type: application/json" \
  -d '{"feed_id":"test", "items":[{"id":"1", "content":"This is outrage!", "timestamp":"2024-01-01"}]}'
```

---

## TOOL 2: PERSONAL VULNERABILITY SCANNER
### Week 2 Implementation

### Step 1: Blink Rate Detection

**File: `src/scanners/blink_detector.py`**

```python
import cv2
import numpy as np
from dlib import get_frontal_face_detector, shape_predictor
import time

class BlinkDetector:
    """Measure blink rate via webcam"""

    def __init__(self):
        # Download face detection models
        self.detector = get_frontal_face_detector()
        # You'll need to download shape_predictor_68_face_landmarks.dat

    def measure_blink_rate(self, duration_seconds=60):
        """
        Measure blinks per minute for duration_seconds
        Returns: blinks_per_minute
        """
        cap = cv2.VideoCapture(0)

        start_time = time.time()
        blink_count = 0
        frame_count = 0

        eye_closed_threshold = 0.2  # EAR threshold
        previous_ear = 1.0

        while (time.time() - start_time) < duration_seconds:
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = self.detector(gray)

            for face in faces:
                # Get eye region (simplified; real implementation uses landmarks)
                # Calculate Eye Aspect Ratio (EAR)
                ear = self.calculate_ear(face)  # Simplified

                # Detect blink (EAR drops below threshold)
                if previous_ear > eye_closed_threshold and ear < eye_closed_threshold:
                    blink_count += 1

                previous_ear = ear

        cap.release()
        cv2.destroyAllWindows()

        elapsed = time.time() - start_time
        bpm = (blink_count / elapsed) * 60

        return {
            'blink_rate_bpm': bpm,
            'blink_count': blink_count,
            'duration_seconds': elapsed,
            'frames_processed': frame_count
        }

    def calculate_ear(self, face):
        """Calculate Eye Aspect Ratio (simplified)"""
        # In production, use dlib landmarks to get precise eye coordinates
        return np.random.random()  # Placeholder
```

### Step 2: Vulnerability Scoring Algorithm

**File: `src/scanners/vulnerability_scorer.py`**

```python
class VulnerabilityScorer:
    """Score vulnerability across all three domains"""

    def score_blink_rate(self, baseline_bpm, minimum_bpm_during_exposure):
        """
        Score blink-rate vulnerability (0-10)
        Lower blink rate during exposure = higher vulnerability
        """
        if baseline_bpm == 0:
            return 0

        drop_percentage = (baseline_bpm - minimum_bpm_during_exposure) / baseline_bpm

        # Convert to 0-10 score
        # 0% drop = 0 points
        # 50% drop = 5 points
        # 100% drop = 10 points

        score = drop_percentage * 10
        return min(10, max(0, score))

    def score_physiological(self, hrv_milliseconds):
        """
        Score physiological vulnerability based on HRV
        Low HRV = high vulnerability
        """
        if hrv_milliseconds > 70:
            return 2  # Low vulnerability
        elif hrv_milliseconds > 50:
            return 4  # Low-moderate
        elif hrv_milliseconds > 35:
            return 6  # Moderate
        elif hrv_milliseconds > 20:
            return 8  # High
        else:
            return 10  # Very high

    def score_personality(self, trait_anxiety, neuroticism, belonging_need):
        """
        Average personality scores (each already 0-10)
        """
        return (trait_anxiety + neuroticism + belonging_need) / 3

    def calculate_overall_vulnerability(self, domain_scores):
        """
        Combine domain scores with weights
        domain_scores: {'blink_rate': X, 'physiological': Y, 'personality': Z}
        """

        weights = {
            'blink_rate': 0.33,
            'physiological': 0.33,
            'personality': 0.34
        }

        overall = sum(
            domain_scores.get(k, 0) * weights[k]
            for k in weights
        )

        return round(overall, 2)
```

### Step 3: Web Interface

**File: `src/web/vulnerability_scanner.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerability Scanner</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Personal Vulnerability Scanner</h1>

    <div id="blink-test">
        <h2>Test 1: Blink Rate</h2>
        <p>Allow camera access and look at the screen for 10 minutes</p>
        <video id="video" width="320" height="240" autoplay></video>
        <button onclick="startBlinkTest()">Start Test</button>
        <p id="blink-result"></p>
    </div>

    <div id="personality-test">
        <h2>Test 2: Personality Assessment</h2>
        <form>
            <h3>Trait Anxiety</h3>
            <label>I worry frequently: <input type="range" min="0" max="10"></label>
            <!-- 4 more questions -->

            <h3>Neuroticism</h3>
            <!-- 5 questions -->

            <h3>Need for Belonging</h3>
            <!-- 5 questions -->

            <button type="button" onclick="submitPersonality()">Submit</button>
        </form>
    </div>

    <div id="results">
        <h2>Your Vulnerability Profile</h2>
        <canvas id="vulnerabilityChart"></canvas>
        <p id="interpretation"></p>
    </div>

    <script src="scanner.js"></script>
</body>
</html>
```

---

## NEXT TOOLS TO BUILD (Weeks 3-4)

Specifications for Tools 3-12 follow the same pattern:
1. Define data schema
2. Write core algorithms
3. Build API endpoints
4. Create tests
5. Deploy

---

## DEVELOPMENT CHECKLIST

### For Each Tool:

- [ ] Requirements gathered and documented
- [ ] Data schema designed
- [ ] Core algorithms implemented
- [ ] 80%+ test coverage
- [ ] API endpoints documented (Swagger/OpenAPI)
- [ ] Deployed to staging environment
- [ ] Performance tested (<1 sec response)
- [ ] Security reviewed (HIPAA/GDPR if needed)
- [ ] Documentation written (README, code comments)
- [ ] Ready for production deployment

---

## COMMON PITFALLS

1. **Over-engineering early**: Start with simple MVP, iterate
2. **Insufficient testing**: Test continuously, not at end
3. **Ignoring deployment**: Plan deployment architecture from day 1
4. **Poor documentation**: Document as you build
5. **Security delays**: Security should be built in, not added later

---

## SUPPORT RESOURCES

- **Python libraries:**
  - NLP: NLTK, spaCy, TextBlob
  - ML: scikit-learn, XGBoost, TensorFlow
  - API: FastAPI, Flask
  - Testing: pytest, unittest

- **Data integration:**
  - Apple HealthKit: `HealthKitManager`
  - Fitbit: Official API documentation
  - Arduino: pySerial library
  - OpenFace: GitHub repository

- **Deployment:**
  - Docker: containerization
  - AWS/GCP/Azure: cloud deployment
  - GitHub Actions: CI/CD pipeline

---

## SUCCESS CRITERIA

You're ready to move to next tool when:
- ✓ MVP works (not perfect, but functional)
- ✓ Can process real data
- ✓ API responds in <1 second
- ✓ Tests pass
- ✓ Documentation complete

**Ship it. Iterate based on feedback. Move to next tool.**

Don't wait for perfection. Perfection kills shipping.

