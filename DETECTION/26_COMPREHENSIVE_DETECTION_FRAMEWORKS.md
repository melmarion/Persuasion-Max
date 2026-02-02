# COMPREHENSIVE DETECTION FRAMEWORKS
## Extended Research & Detection Code for Persuasion Auditing

**Document Version:** 1.0
**Created:** February 2025
**Purpose:** Complete detection frameworks for all identified manipulation mechanisms

---

## TABLE OF CONTENTS

1. [Multimodal Persuasion Mechanics](#1-multimodal-persuasion-mechanics)
2. [Social Network Dynamics](#2-social-network-dynamics)
3. [Trust Architecture & Exploitation](#3-trust-architecture--exploitation)
4. [Platform-Specific Mechanics](#4-platform-specific-mechanics)
5. [Physiological Validation Methods](#5-physiological-validation-methods)
6. [Vulnerable Population Detection](#6-vulnerable-population-detection)
7. [Economic Manipulation Mechanics](#7-economic-manipulation-mechanics)
8. [AI-Specific Manipulation](#8-ai-specific-manipulation)
9. [Intervention Effectiveness Analysis](#9-intervention-effectiveness-analysis)
10. [Regulatory Compliance Mapping](#10-regulatory-compliance-mapping)

---

## 1. MULTIMODAL PERSUASION MECHANICS

### Research Findings

**Audio Manipulation:**
- Voice tone affects perceived competence and persuasiveness
- Low-pitched voices perceived as more competent, authoritative (Personality and Social Psychology Bulletin, 2024)
- Falling intonation signals confidence and increases elaboration likelihood
- ASMR triggers (whispering, tapping) activate relaxation responses and reduce critical processing

**Video Editing Patterns:**
- Cut frequency of 2.5-3 seconds creates "attentional synchrony"
- Rapid cuts (5-10 in sequence) followed by calm pacing creates "stimulate → calm → re-engage" cycle
- Chaotic/fast audiovisuals increase attentional scope but DECREASE conscious processing
- Alpha rhythm increases after cuts, indicating reduced analytical engagement

**Color Psychology:**
- Colors influence 85-90% of initial purchase impressions
- Red: Urgency, passion, danger - makes time feel slower, objects heavier
- Blue: Trust, calm - time passes quickly, objects feel lighter
- Yellow: Optimism, attention-grabbing (left brain stimulation)

```python
import numpy as np
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
import re

class AudioManipulationType(Enum):
    VOICE_PITCH_LOW = "low_pitch_authority"
    VOICE_PITCH_VARIATION = "pitch_manipulation"
    FALLING_INTONATION = "confidence_signal"
    ASMR_TRIGGERS = "asmr_relaxation"
    URGENCY_TONE = "urgency_pressure"
    WHISPER = "intimacy_whisper"
    BACKGROUND_MUSIC_TEMPO = "tempo_manipulation"

class VideoManipulationType(Enum):
    RAPID_CUTS = "attention_fragmentation"
    ZOOM_FOCUS = "attention_direction"
    RHYTHM_PATTERN = "emotional_pacing"
    FLASH_FRAMES = "subliminal_priming"
    EYE_CONTACT = "parasocial_connection"
    COLOR_GRADING = "mood_manipulation"

@dataclass
class AudioAnalysisResult:
    """Results from audio manipulation analysis"""
    pitch_mean: float = 0.0
    pitch_variance: float = 0.0
    intonation_pattern: str = ""
    tempo_bpm: float = 0.0
    asmr_trigger_count: int = 0
    whisper_segments: int = 0
    urgency_markers: int = 0
    manipulation_types: List[AudioManipulationType] = field(default_factory=list)
    risk_score: float = 0.0

@dataclass
class VideoAnalysisResult:
    """Results from video manipulation analysis"""
    avg_shot_length: float = 0.0
    cut_frequency: float = 0.0
    rapid_cut_sequences: int = 0
    zoom_events: int = 0
    eye_contact_duration: float = 0.0
    dominant_colors: List[str] = field(default_factory=list)
    color_manipulation_score: float = 0.0
    manipulation_types: List[VideoManipulationType] = field(default_factory=list)
    risk_score: float = 0.0

class MultimodalPersuasionDetector:
    """
    Detects manipulation techniques in audio-visual content.

    Research basis:
    - ICMI 2025: Multimodal persuasion combines emotion, cognition, personality factors
    - 2024 voice research: Low pitch increases perceived competence
    - Film editing research: Cuts affect alpha rhythm and conscious processing
    """

    # ASMR trigger words/sounds that reduce critical processing
    ASMR_TRIGGERS = [
        'whisper', 'tapping', 'scratching', 'brushing', 'crinkling',
        'soft spoken', 'gentle', 'relaxing', 'soothing', 'tingles'
    ]

    # Urgency audio markers
    URGENCY_AUDIO_MARKERS = [
        'now', 'immediately', 'hurry', 'quick', 'fast', 'limited time',
        'act now', 'don\'t wait', 'today only', 'expires'
    ]

    # Color associations for manipulation detection
    COLOR_PSYCHOLOGY = {
        'red': {'emotions': ['urgency', 'excitement', 'danger'], 'manipulation_potential': 0.8},
        'orange': {'emotions': ['enthusiasm', 'warmth'], 'manipulation_potential': 0.5},
        'yellow': {'emotions': ['optimism', 'attention'], 'manipulation_potential': 0.6},
        'green': {'emotions': ['trust', 'nature', 'money'], 'manipulation_potential': 0.4},
        'blue': {'emotions': ['trust', 'calm', 'security'], 'manipulation_potential': 0.3},
        'purple': {'emotions': ['luxury', 'creativity'], 'manipulation_potential': 0.5},
        'black': {'emotions': ['sophistication', 'power'], 'manipulation_potential': 0.4},
        'white': {'emotions': ['purity', 'simplicity'], 'manipulation_potential': 0.2},
    }

    def __init__(self):
        self.thresholds = {
            'low_pitch_hz': 120,  # Below this = authority voice
            'high_pitch_variance': 50,  # High variance = emotional manipulation
            'rapid_cut_threshold': 2.0,  # Seconds - below this is rapid
            'burst_sequence_min': 5,  # Minimum cuts for "burst sequence"
            'asmr_trigger_threshold': 3,  # Multiple triggers = intentional
            'eye_contact_manipulation': 0.4,  # 40%+ of video = parasocial building
        }

    def analyze_audio_features(self, audio_data: Dict) -> AudioAnalysisResult:
        """
        Analyze audio for manipulation techniques.

        Expected audio_data format:
        {
            'pitch_values': [float],  # Hz values over time
            'transcript': str,
            'tempo_bpm': float,
            'volume_envelope': [float],
            'segments': [{'start': float, 'end': float, 'type': str}]
        }
        """
        result = AudioAnalysisResult()

        # Pitch analysis
        if 'pitch_values' in audio_data and audio_data['pitch_values']:
            pitches = np.array(audio_data['pitch_values'])
            result.pitch_mean = float(np.mean(pitches))
            result.pitch_variance = float(np.var(pitches))

            # Low pitch authority detection
            if result.pitch_mean < self.thresholds['low_pitch_hz']:
                result.manipulation_types.append(AudioManipulationType.VOICE_PITCH_LOW)
                result.risk_score += 0.3

            # High variance = emotional manipulation
            if result.pitch_variance > self.thresholds['high_pitch_variance']:
                result.manipulation_types.append(AudioManipulationType.VOICE_PITCH_VARIATION)
                result.risk_score += 0.4

        # Transcript analysis for ASMR triggers
        if 'transcript' in audio_data:
            transcript_lower = audio_data['transcript'].lower()

            for trigger in self.ASMR_TRIGGERS:
                if trigger in transcript_lower:
                    result.asmr_trigger_count += 1

            if result.asmr_trigger_count >= self.thresholds['asmr_trigger_threshold']:
                result.manipulation_types.append(AudioManipulationType.ASMR_TRIGGERS)
                result.risk_score += 0.5

            # Urgency markers
            for marker in self.URGENCY_AUDIO_MARKERS:
                if marker in transcript_lower:
                    result.urgency_markers += 1

            if result.urgency_markers >= 3:
                result.manipulation_types.append(AudioManipulationType.URGENCY_TONE)
                result.risk_score += 0.4

        # Tempo analysis
        if 'tempo_bpm' in audio_data:
            result.tempo_bpm = audio_data['tempo_bpm']
            # Fast tempo (>120 BPM) creates excitement/urgency
            if result.tempo_bpm > 120:
                result.manipulation_types.append(AudioManipulationType.BACKGROUND_MUSIC_TEMPO)
                result.risk_score += 0.2

        # Whisper segment detection
        if 'segments' in audio_data:
            result.whisper_segments = sum(
                1 for seg in audio_data['segments']
                if seg.get('type') == 'whisper'
            )
            if result.whisper_segments > 0:
                result.manipulation_types.append(AudioManipulationType.WHISPER)
                result.risk_score += 0.3

        # Intonation pattern (falling = confidence)
        if 'pitch_values' in audio_data and len(audio_data['pitch_values']) > 10:
            # Check if pitch generally falls at end of phrases
            last_quarter = audio_data['pitch_values'][-len(audio_data['pitch_values'])//4:]
            if np.mean(last_quarter) < result.pitch_mean * 0.9:
                result.intonation_pattern = "falling"
                result.manipulation_types.append(AudioManipulationType.FALLING_INTONATION)
                result.risk_score += 0.2

        result.risk_score = min(1.0, result.risk_score)
        return result

    def analyze_video_features(self, video_data: Dict) -> VideoAnalysisResult:
        """
        Analyze video for manipulation techniques.

        Expected video_data format:
        {
            'cuts': [float],  # Timestamps of cuts
            'duration': float,
            'zoom_events': [{'time': float, 'type': str}],
            'face_detections': [{'time': float, 'eye_contact': bool}],
            'color_histogram': {'red': float, 'green': float, 'blue': float, ...}
        }
        """
        result = VideoAnalysisResult()

        # Cut analysis
        if 'cuts' in video_data and 'duration' in video_data:
            cuts = video_data['cuts']
            duration = video_data['duration']

            if len(cuts) > 1:
                # Calculate inter-cut intervals
                intervals = np.diff(cuts)
                result.avg_shot_length = float(np.mean(intervals))
                result.cut_frequency = len(cuts) / duration * 60  # Cuts per minute

                # Detect rapid cut sequences (burst sequences)
                rapid_cuts = intervals < self.thresholds['rapid_cut_threshold']

                # Count consecutive rapid cuts
                consecutive_count = 0
                max_consecutive = 0
                burst_sequences = 0

                for is_rapid in rapid_cuts:
                    if is_rapid:
                        consecutive_count += 1
                        max_consecutive = max(max_consecutive, consecutive_count)
                    else:
                        if consecutive_count >= self.thresholds['burst_sequence_min']:
                            burst_sequences += 1
                        consecutive_count = 0

                result.rapid_cut_sequences = burst_sequences

                if result.avg_shot_length < 3.0:
                    result.manipulation_types.append(VideoManipulationType.RAPID_CUTS)
                    result.risk_score += 0.4

                if burst_sequences > 0:
                    result.manipulation_types.append(VideoManipulationType.RHYTHM_PATTERN)
                    result.risk_score += 0.3

        # Zoom event analysis
        if 'zoom_events' in video_data:
            result.zoom_events = len(video_data['zoom_events'])
            if result.zoom_events > 10:  # Frequent zooms
                result.manipulation_types.append(VideoManipulationType.ZOOM_FOCUS)
                result.risk_score += 0.2

        # Eye contact analysis (parasocial relationship building)
        if 'face_detections' in video_data and 'duration' in video_data:
            eye_contact_frames = sum(
                1 for f in video_data['face_detections']
                if f.get('eye_contact', False)
            )
            total_frames = len(video_data['face_detections'])

            if total_frames > 0:
                result.eye_contact_duration = eye_contact_frames / total_frames

                if result.eye_contact_duration > self.thresholds['eye_contact_manipulation']:
                    result.manipulation_types.append(VideoManipulationType.EYE_CONTACT)
                    result.risk_score += 0.3

        # Color analysis
        if 'color_histogram' in video_data:
            histogram = video_data['color_histogram']
            total = sum(histogram.values())

            if total > 0:
                for color, value in histogram.items():
                    proportion = value / total
                    if proportion > 0.3:  # Dominant color
                        result.dominant_colors.append(color)
                        if color in self.COLOR_PSYCHOLOGY:
                            result.color_manipulation_score += (
                                self.COLOR_PSYCHOLOGY[color]['manipulation_potential'] * proportion
                            )

                if result.color_manipulation_score > 0.5:
                    result.manipulation_types.append(VideoManipulationType.COLOR_GRADING)
                    result.risk_score += result.color_manipulation_score * 0.3

        result.risk_score = min(1.0, result.risk_score)
        return result

    def analyze_audiovisual_synchronization(
        self,
        audio_result: AudioAnalysisResult,
        video_result: VideoAnalysisResult
    ) -> Dict:
        """
        Analyze how audio and video work together for manipulation.

        Research: Audio-visual synchronization amplifies emotional impact
        (ICMI 2025, MMS-LLaMA research)
        """
        sync_analysis = {
            'combined_risk_score': 0.0,
            'synergy_detected': False,
            'manipulation_amplification': 1.0,
            'findings': []
        }

        # Base combined score
        sync_analysis['combined_risk_score'] = (
            audio_result.risk_score * 0.4 +
            video_result.risk_score * 0.4
        )

        # Check for synergistic combinations
        synergies = []

        # ASMR audio + slow video = deep relaxation (reduced critical thinking)
        if (AudioManipulationType.ASMR_TRIGGERS in audio_result.manipulation_types and
            video_result.avg_shot_length > 5.0):
            synergies.append("ASMR_RELAXATION_COMBO")
            sync_analysis['manipulation_amplification'] *= 1.4

        # Urgency audio + rapid cuts = heightened anxiety
        if (AudioManipulationType.URGENCY_TONE in audio_result.manipulation_types and
            VideoManipulationType.RAPID_CUTS in video_result.manipulation_types):
            synergies.append("URGENCY_ANXIETY_COMBO")
            sync_analysis['manipulation_amplification'] *= 1.5

        # Authority voice + eye contact = trust exploitation
        if (AudioManipulationType.VOICE_PITCH_LOW in audio_result.manipulation_types and
            VideoManipulationType.EYE_CONTACT in video_result.manipulation_types):
            synergies.append("AUTHORITY_TRUST_COMBO")
            sync_analysis['manipulation_amplification'] *= 1.3

        # Fast tempo + rapid cuts = overstimulation
        if (AudioManipulationType.BACKGROUND_MUSIC_TEMPO in audio_result.manipulation_types and
            VideoManipulationType.RAPID_CUTS in video_result.manipulation_types):
            synergies.append("OVERSTIMULATION_COMBO")
            sync_analysis['manipulation_amplification'] *= 1.4

        if synergies:
            sync_analysis['synergy_detected'] = True
            sync_analysis['findings'] = synergies
            sync_analysis['combined_risk_score'] *= sync_analysis['manipulation_amplification']

        sync_analysis['combined_risk_score'] = min(1.0, sync_analysis['combined_risk_score'])

        return sync_analysis


class CutRhythmAnalyzer:
    """
    Specialized analyzer for video editing rhythm patterns.

    Research basis:
    - Film editing affects alpha rhythm and conscious processing
    - "Stimulate → calm → re-engage" pattern keeps viewers engaged
    - Modern content: 2.5-3 second average shot length
    """

    def __init__(self):
        self.patterns = {
            'commercial': {'avg_shot': 2.0, 'burst_freq': 'high'},
            'documentary': {'avg_shot': 8.0, 'burst_freq': 'low'},
            'social_media': {'avg_shot': 1.5, 'burst_freq': 'very_high'},
            'manipulative': {'avg_shot': 2.5, 'burst_freq': 'strategic'}
        }

    def analyze_rhythm_pattern(self, cut_timestamps: List[float], duration: float) -> Dict:
        """
        Analyze the rhythm pattern of video cuts.

        Returns pattern classification and manipulation indicators.
        """
        if len(cut_timestamps) < 3:
            return {'pattern': 'minimal', 'manipulation_score': 0.0}

        intervals = np.diff(cut_timestamps)

        analysis = {
            'avg_interval': float(np.mean(intervals)),
            'std_interval': float(np.std(intervals)),
            'min_interval': float(np.min(intervals)),
            'max_interval': float(np.max(intervals)),
            'cuts_per_minute': len(cut_timestamps) / duration * 60,
            'pattern_type': '',
            'manipulation_indicators': [],
            'manipulation_score': 0.0
        }

        # Detect "stimulate → calm → re-engage" pattern
        # Look for alternating fast/slow sequences
        window_size = 5
        if len(intervals) >= window_size * 2:
            window_means = [
                np.mean(intervals[i:i+window_size])
                for i in range(0, len(intervals) - window_size, window_size)
            ]

            # Check for significant variance between windows (pattern switching)
            if len(window_means) >= 2:
                window_variance = np.var(window_means)
                if window_variance > 2.0:  # High variance = intentional rhythm manipulation
                    analysis['manipulation_indicators'].append('RHYTHM_MANIPULATION')
                    analysis['manipulation_score'] += 0.4

        # Detect hypnotic regularity (very consistent rhythm)
        cv = analysis['std_interval'] / analysis['avg_interval'] if analysis['avg_interval'] > 0 else 0
        if cv < 0.2:  # Very consistent timing
            analysis['manipulation_indicators'].append('HYPNOTIC_REGULARITY')
            analysis['manipulation_score'] += 0.3

        # Detect acceleration patterns (building urgency)
        if len(intervals) >= 10:
            first_half = np.mean(intervals[:len(intervals)//2])
            second_half = np.mean(intervals[len(intervals)//2:])

            if second_half < first_half * 0.7:  # 30%+ acceleration
                analysis['manipulation_indicators'].append('URGENCY_ACCELERATION')
                analysis['manipulation_score'] += 0.4

        # Classify pattern type
        if analysis['avg_interval'] < 2.0:
            analysis['pattern_type'] = 'high_intensity'
        elif analysis['avg_interval'] < 4.0:
            analysis['pattern_type'] = 'commercial'
        elif analysis['avg_interval'] < 8.0:
            analysis['pattern_type'] = 'moderate'
        else:
            analysis['pattern_type'] = 'slow_pace'

        analysis['manipulation_score'] = min(1.0, analysis['manipulation_score'])

        return analysis
```

---

## 2. SOCIAL NETWORK DYNAMICS

### Research Findings

**Cascade Effects (2024-2025):**
- Misinformation follows 4 phases: introduction, acceleration, saturation, stabilization
- Confirmation bias + algorithmic personalization creates echo chambers
- Homogeneity is the primary driver of content diffusion
- Temporal graph analysis shows community evolution during cascades

**Bot Networks:**
- 50%+ of internet traffic is now automated bots (2024)
- 76% detection failure rate for advanced AI bots
- Bot farms use real phones with SIM cards to evade detection
- AI swarms coordinate and adapt tactics in real-time

**Emotional Contagion:**
- Negative posts evoke more attention and are more persistent
- 4.34% over-exposure to negative content precedes negative posting
- Massive-scale emotional manipulation is technically feasible

```python
@dataclass
class CascadeMetrics:
    """Metrics for information cascade analysis"""
    reach: int = 0
    depth: int = 0
    velocity: float = 0.0  # Shares per hour
    homogeneity_score: float = 0.0
    bot_participation_rate: float = 0.0
    phase: str = ""  # introduction, acceleration, saturation, stabilization
    echo_chamber_score: float = 0.0

@dataclass
class AccountSuspicionScore:
    """Suspicion scoring for potential bot/fake accounts"""
    account_id: str = ""
    creation_recency: float = 0.0
    posting_regularity: float = 0.0
    engagement_ratio: float = 0.0
    content_originality: float = 0.0
    network_clustering: float = 0.0
    temporal_patterns: float = 0.0
    overall_bot_probability: float = 0.0

class SocialNetworkManipulationDetector:
    """
    Detects manipulation patterns in social network dynamics.

    Research basis:
    - Springer 2025: Cascading falsehoods mapping
    - Nature 2026: Temporal graph analysis of fake news cascades
    - Frontiers 2025: Multi-scenario misinformation modeling
    - NATO StratCom 2024: Social media manipulation for sale
    """

    def __init__(self):
        # Thresholds based on research
        self.thresholds = {
            'bot_posting_regularity': 0.95,  # >95% regular = suspicious
            'engagement_ratio_low': 0.001,  # Very low engagement = fake followers
            'engagement_ratio_high': 0.5,  # Very high = coordinated
            'cascade_velocity_viral': 1000,  # Shares per hour
            'homogeneity_echo_chamber': 0.8,  # >80% similar = echo chamber
            'coordination_window': 60,  # Seconds - posts within this = coordinated
        }

        # Bot behavior patterns
        self.bot_indicators = {
            'perfect_timing': 0.3,  # Posts at exact intervals
            'no_typos': 0.1,  # Never makes mistakes
            'rapid_response': 0.2,  # Responds within seconds
            'template_content': 0.3,  # Repetitive phrasing
            'unusual_hours': 0.2,  # Active 24/7
            'network_clustering': 0.3,  # Connected mainly to other bots
        }

    def analyze_cascade(self, posts: List[Dict]) -> CascadeMetrics:
        """
        Analyze an information cascade for manipulation indicators.

        Expected post format:
        {
            'id': str,
            'timestamp': float,
            'author_id': str,
            'content': str,
            'parent_id': Optional[str],
            'engagement': {'likes': int, 'shares': int, 'comments': int}
        }
        """
        if not posts:
            return CascadeMetrics()

        metrics = CascadeMetrics()

        # Sort by timestamp
        sorted_posts = sorted(posts, key=lambda x: x['timestamp'])

        # Calculate reach (unique authors)
        unique_authors = set(p['author_id'] for p in posts)
        metrics.reach = len(unique_authors)

        # Calculate depth (longest chain)
        metrics.depth = self._calculate_cascade_depth(posts)

        # Calculate velocity
        if len(sorted_posts) >= 2:
            time_span = sorted_posts[-1]['timestamp'] - sorted_posts[0]['timestamp']
            if time_span > 0:
                hours = time_span / 3600
                metrics.velocity = len(posts) / hours

        # Determine phase based on velocity patterns
        metrics.phase = self._determine_cascade_phase(sorted_posts)

        # Calculate homogeneity (content similarity)
        metrics.homogeneity_score = self._calculate_content_homogeneity(posts)

        # Echo chamber detection
        if metrics.homogeneity_score > self.thresholds['homogeneity_echo_chamber']:
            metrics.echo_chamber_score = metrics.homogeneity_score

        # Estimate bot participation
        metrics.bot_participation_rate = self._estimate_bot_participation(posts)

        return metrics

    def _calculate_cascade_depth(self, posts: List[Dict]) -> int:
        """Calculate the maximum depth of the reply/share chain"""
        # Build parent-child relationships
        children = {}
        roots = []

        for post in posts:
            parent = post.get('parent_id')
            if parent:
                if parent not in children:
                    children[parent] = []
                children[parent].append(post['id'])
            else:
                roots.append(post['id'])

        # BFS to find max depth
        max_depth = 0
        queue = [(root, 1) for root in roots]

        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)

            if node in children:
                for child in children[node]:
                    queue.append((child, depth + 1))

        return max_depth

    def _determine_cascade_phase(self, sorted_posts: List[Dict]) -> str:
        """
        Determine cascade phase based on velocity patterns.

        Phases from research:
        - Introduction: Initial slow spread
        - Acceleration: Rapid growth
        - Saturation: Peak reached
        - Stabilization: Decline to baseline
        """
        if len(sorted_posts) < 10:
            return "introduction"

        # Divide into quarters and calculate velocity for each
        quarter_size = len(sorted_posts) // 4
        velocities = []

        for i in range(4):
            start_idx = i * quarter_size
            end_idx = (i + 1) * quarter_size if i < 3 else len(sorted_posts)
            quarter = sorted_posts[start_idx:end_idx]

            if len(quarter) >= 2:
                time_span = quarter[-1]['timestamp'] - quarter[0]['timestamp']
                if time_span > 0:
                    velocities.append(len(quarter) / (time_span / 3600))
                else:
                    velocities.append(0)

        if len(velocities) < 4:
            return "introduction"

        # Analyze velocity pattern
        if velocities[1] > velocities[0] * 1.5:
            if velocities[2] < velocities[1]:
                if velocities[3] < velocities[2]:
                    return "stabilization"
                return "saturation"
            return "acceleration"

        return "introduction"

    def _calculate_content_homogeneity(self, posts: List[Dict]) -> float:
        """Calculate how similar the content is across posts"""
        if len(posts) < 2:
            return 0.0

        contents = [p.get('content', '') for p in posts if p.get('content')]
        if len(contents) < 2:
            return 0.0

        # Simple word overlap calculation
        word_sets = [set(c.lower().split()) for c in contents]

        total_similarity = 0
        comparisons = 0

        for i in range(len(word_sets)):
            for j in range(i + 1, len(word_sets)):
                if word_sets[i] and word_sets[j]:
                    intersection = len(word_sets[i] & word_sets[j])
                    union = len(word_sets[i] | word_sets[j])
                    if union > 0:
                        total_similarity += intersection / union
                        comparisons += 1

        return total_similarity / comparisons if comparisons > 0 else 0.0

    def _estimate_bot_participation(self, posts: List[Dict]) -> float:
        """Estimate the percentage of posts from likely bots"""
        if not posts:
            return 0.0

        suspicious_posts = 0

        # Group posts by author
        author_posts = {}
        for post in posts:
            author = post['author_id']
            if author not in author_posts:
                author_posts[author] = []
            author_posts[author].append(post)

        for author, author_post_list in author_posts.items():
            suspicion = 0.0

            # Check posting regularity
            if len(author_post_list) >= 3:
                timestamps = sorted([p['timestamp'] for p in author_post_list])
                intervals = np.diff(timestamps)

                if len(intervals) >= 2:
                    cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) > 0 else 0
                    if cv < 0.1:  # Very regular posting
                        suspicion += self.bot_indicators['perfect_timing']

            # Check for rapid responses
            for post in author_post_list:
                if post.get('parent_id'):
                    # Find parent timestamp
                    parent = next((p for p in posts if p['id'] == post['parent_id']), None)
                    if parent:
                        response_time = post['timestamp'] - parent['timestamp']
                        if response_time < 5:  # Less than 5 seconds
                            suspicion += self.bot_indicators['rapid_response']
                            break

            if suspicion > 0.3:
                suspicious_posts += len(author_post_list)

        return suspicious_posts / len(posts) if posts else 0.0

    def detect_coordinated_behavior(self, posts: List[Dict]) -> Dict:
        """
        Detect coordinated inauthentic behavior patterns.

        Research: Meta's "coordinated inauthentic behavior" detection
        """
        coordination_analysis = {
            'coordinated_clusters': [],
            'coordination_score': 0.0,
            'suspected_bot_farm': False,
            'temporal_anomalies': [],
            'content_similarity_clusters': []
        }

        # Group by timestamp windows
        window = self.thresholds['coordination_window']
        sorted_posts = sorted(posts, key=lambda x: x['timestamp'])

        clusters = []
        current_cluster = [sorted_posts[0]] if sorted_posts else []

        for i in range(1, len(sorted_posts)):
            if sorted_posts[i]['timestamp'] - sorted_posts[i-1]['timestamp'] <= window:
                current_cluster.append(sorted_posts[i])
            else:
                if len(current_cluster) >= 3:
                    clusters.append(current_cluster)
                current_cluster = [sorted_posts[i]]

        if len(current_cluster) >= 3:
            clusters.append(current_cluster)

        # Analyze clusters for coordination
        for cluster in clusters:
            unique_authors = len(set(p['author_id'] for p in cluster))

            # Many posts from different authors in short window = suspicious
            if unique_authors >= 3 and len(cluster) >= 5:
                content_similarity = self._calculate_content_homogeneity(cluster)

                if content_similarity > 0.5:  # Similar content = coordinated
                    coordination_analysis['coordinated_clusters'].append({
                        'size': len(cluster),
                        'unique_authors': unique_authors,
                        'similarity': content_similarity,
                        'time_window': cluster[-1]['timestamp'] - cluster[0]['timestamp']
                    })

        # Calculate overall coordination score
        if coordination_analysis['coordinated_clusters']:
            coordination_analysis['coordination_score'] = min(1.0,
                len(coordination_analysis['coordinated_clusters']) * 0.2 +
                sum(c['similarity'] for c in coordination_analysis['coordinated_clusters']) /
                len(coordination_analysis['coordinated_clusters']) * 0.5
            )

            # High coordination with similar content = bot farm
            if coordination_analysis['coordination_score'] > 0.7:
                coordination_analysis['suspected_bot_farm'] = True

        return coordination_analysis


class EmotionalContagionDetector:
    """
    Detects emotional contagion patterns in social media content.

    Research basis:
    - PNAS Facebook study: Emotional contagion at massive scale
    - 2024 research: Negative posts more persistent and contagious
    - 4.34% over-exposure to negative content precedes negative posting
    """

    EMOTION_KEYWORDS = {
        'anger': ['angry', 'furious', 'outraged', 'hate', 'disgusted', 'infuriated'],
        'fear': ['scared', 'afraid', 'terrified', 'worried', 'anxious', 'panic'],
        'sadness': ['sad', 'depressed', 'hopeless', 'miserable', 'devastated'],
        'joy': ['happy', 'excited', 'thrilled', 'delighted', 'ecstatic', 'amazing'],
        'surprise': ['shocked', 'stunned', 'amazed', 'unbelievable', 'wow'],
        'disgust': ['disgusting', 'gross', 'revolting', 'sickening', 'appalling']
    }

    def __init__(self):
        self.negative_emotions = ['anger', 'fear', 'sadness', 'disgust']
        self.positive_emotions = ['joy', 'surprise']

    def analyze_emotional_content(self, posts: List[Dict]) -> Dict:
        """Analyze emotional content distribution and patterns"""
        analysis = {
            'emotion_distribution': {},
            'negativity_ratio': 0.0,
            'emotional_intensity': 0.0,
            'contagion_risk_score': 0.0,
            'manipulation_indicators': []
        }

        emotion_counts = {emotion: 0 for emotion in self.EMOTION_KEYWORDS}
        total_emotional_posts = 0

        for post in posts:
            content = post.get('content', '').lower()
            post_emotions = []

            for emotion, keywords in self.EMOTION_KEYWORDS.items():
                if any(kw in content for kw in keywords):
                    emotion_counts[emotion] += 1
                    post_emotions.append(emotion)

            if post_emotions:
                total_emotional_posts += 1

        if total_emotional_posts > 0:
            analysis['emotion_distribution'] = {
                emotion: count / total_emotional_posts
                for emotion, count in emotion_counts.items()
            }

            # Calculate negativity ratio
            negative_count = sum(emotion_counts[e] for e in self.negative_emotions)
            positive_count = sum(emotion_counts[e] for e in self.positive_emotions)
            total = negative_count + positive_count

            if total > 0:
                analysis['negativity_ratio'] = negative_count / total

            # Emotional intensity (proportion of posts with strong emotion)
            analysis['emotional_intensity'] = total_emotional_posts / len(posts)

            # Contagion risk assessment
            # High negativity + high intensity = high contagion risk
            analysis['contagion_risk_score'] = (
                analysis['negativity_ratio'] * 0.5 +
                analysis['emotional_intensity'] * 0.3 +
                (emotion_counts['anger'] / total_emotional_posts) * 0.2  # Anger most contagious
            )

            # Detect manipulation patterns
            if analysis['negativity_ratio'] > 0.7:
                analysis['manipulation_indicators'].append('HIGH_NEGATIVITY_BIAS')

            if emotion_counts['anger'] > emotion_counts['fear'] * 2:
                analysis['manipulation_indicators'].append('ANGER_AMPLIFICATION')

            # Check for emotional sequencing (fractionation)
            if self._detect_emotional_cycling(posts):
                analysis['manipulation_indicators'].append('EMOTIONAL_CYCLING_DETECTED')
                analysis['contagion_risk_score'] += 0.2

        analysis['contagion_risk_score'] = min(1.0, analysis['contagion_risk_score'])

        return analysis

    def _detect_emotional_cycling(self, posts: List[Dict]) -> bool:
        """Detect rapid emotional shifts (fractionation pattern)"""
        if len(posts) < 5:
            return False

        emotions_sequence = []

        for post in posts:
            content = post.get('content', '').lower()
            dominant_emotion = None

            for emotion, keywords in self.EMOTION_KEYWORDS.items():
                if any(kw in content for kw in keywords):
                    dominant_emotion = emotion
                    break

            if dominant_emotion:
                valence = 'negative' if dominant_emotion in self.negative_emotions else 'positive'
                emotions_sequence.append(valence)

        # Count valence switches
        switches = 0
        for i in range(1, len(emotions_sequence)):
            if emotions_sequence[i] != emotions_sequence[i-1]:
                switches += 1

        # High switch rate = emotional sequencing
        switch_rate = switches / len(emotions_sequence) if emotions_sequence else 0

        return switch_rate > 0.4  # More than 40% switches


class EchoChAmberDetector:
    """
    Detects echo chamber formation and filter bubble effects.

    Research basis:
    - PNAS: Polarized information ecosystems reorganize networks via cascades
    - 2024: Homogeneity is preferential driver for content diffusion
    """

    def analyze_information_ecosystem(self, user_feed: List[Dict], network_data: Dict) -> Dict:
        """
        Analyze user's information ecosystem for echo chamber characteristics.

        Expected formats:
        user_feed: [{'content': str, 'source': str, 'stance': str, 'timestamp': float}]
        network_data: {'connections': [str], 'interaction_counts': {str: int}}
        """
        analysis = {
            'viewpoint_diversity': 0.0,
            'source_diversity': 0.0,
            'echo_chamber_score': 0.0,
            'filter_bubble_indicators': [],
            'exposure_bias': {}
        }

        if not user_feed:
            return analysis

        # Analyze viewpoint diversity
        stances = [item.get('stance') for item in user_feed if item.get('stance')]
        if stances:
            unique_stances = set(stances)
            stance_counts = {s: stances.count(s) for s in unique_stances}

            # Shannon entropy for diversity
            total = len(stances)
            entropy = 0
            for count in stance_counts.values():
                if count > 0:
                    p = count / total
                    entropy -= p * np.log2(p)

            # Normalize to 0-1 (max entropy = log2(n_stances))
            max_entropy = np.log2(len(unique_stances)) if len(unique_stances) > 1 else 1
            analysis['viewpoint_diversity'] = entropy / max_entropy if max_entropy > 0 else 0

        # Analyze source diversity
        sources = [item.get('source') for item in user_feed if item.get('source')]
        if sources:
            unique_sources = set(sources)
            analysis['source_diversity'] = len(unique_sources) / len(sources)

        # Calculate echo chamber score (inverse of diversity)
        analysis['echo_chamber_score'] = 1 - (
            analysis['viewpoint_diversity'] * 0.6 +
            analysis['source_diversity'] * 0.4
        )

        # Detect filter bubble indicators
        if analysis['viewpoint_diversity'] < 0.3:
            analysis['filter_bubble_indicators'].append('LOW_VIEWPOINT_DIVERSITY')

        if analysis['source_diversity'] < 0.2:
            analysis['filter_bubble_indicators'].append('SOURCE_CONCENTRATION')

        # Check for algorithmic amplification patterns
        if len(user_feed) >= 20:
            recent = user_feed[-10:]
            older = user_feed[:10]

            recent_diversity = len(set(item.get('stance') for item in recent if item.get('stance')))
            older_diversity = len(set(item.get('stance') for item in older if item.get('stance')))

            if recent_diversity < older_diversity * 0.7:
                analysis['filter_bubble_indicators'].append('NARROWING_EXPOSURE')

        return analysis
```

---

## 3. TRUST ARCHITECTURE & EXPLOITATION

### Research Findings

**Trust Development Processes (2024):**
- Two primary trust mechanisms exploited: relationship history and future expectations
- Future expectations (rewards, urgency, threats) dominate phishing tactics
- Trust is a critical antecedent for unethical behavior exploitation
- Social engineering 2.0: 98% of cyberattacks involve human manipulation

**Grooming Patterns:**
- Predictable stages: victim selection → trust building → desensitization → exploitation
- Vulnerable targets: emotional isolation, low self-esteem, weak support systems
- Gradual escalation: small requests before large exploitative ones

**Trust Exploitation Tactics:**
- Affinity fraud (shared group membership)
- Authority impersonation
- Reciprocity manipulation (unsolicited gifts)
- Commitment escalation (foot-in-the-door)

```python
class TrustExploitationType(Enum):
    RELATIONSHIP_HISTORY = "exploiting_past_relationship"
    FUTURE_EXPECTATIONS = "promises_threats_rewards"
    AUTHORITY_IMPERSONATION = "fake_authority"
    AFFINITY_FRAUD = "shared_group_exploitation"
    RECIPROCITY_TRIGGER = "unsolicited_gift_obligation"
    COMMITMENT_ESCALATION = "foot_in_door"
    URGENCY_PRESSURE = "time_pressure_trust_bypass"
    SOCIAL_PROOF_FABRICATION = "fake_endorsements"

@dataclass
class TrustManipulationIndicator:
    """Indicators of trust-based manipulation"""
    exploitation_type: TrustExploitationType
    confidence: float
    evidence: List[str]
    risk_level: str  # low, medium, high, critical

@dataclass
class GroomingStageAnalysis:
    """Analysis of potential grooming behavior"""
    stage: str  # selection, trust_building, desensitization, exploitation
    indicators: List[str]
    progression_velocity: float  # How fast moving through stages
    risk_score: float

class TrustExploitationDetector:
    """
    Detects patterns of trust building and exploitation.

    Research basis:
    - ACIG Journal 2024: Trust framework for cybersecurity exploitation
    - Wharton 2015: Trust promotes unethical behavior research
    - 2024: Social Engineering 2.0 - 98% of attacks involve manipulation
    """

    # Patterns that indicate trust exploitation attempts
    AUTHORITY_SIGNALS = [
        'official', 'authorized', 'verified', 'certified', 'government',
        'security', 'admin', 'support', 'department', 'representative',
        'manager', 'director', 'compliance', 'legal'
    ]

    URGENCY_SIGNALS = [
        'immediately', 'urgent', 'expire', 'deadline', 'last chance',
        'act now', 'limited time', 'don\'t delay', 'critical', 'emergency',
        'within 24 hours', 'account suspended', 'security alert'
    ]

    RECIPROCITY_SIGNALS = [
        'free gift', 'bonus', 'reward', 'exclusive offer', 'selected',
        'lucky winner', 'complimentary', 'no obligation', 'as a thank you'
    ]

    AFFINITY_SIGNALS = [
        'fellow', 'community', 'member', 'family', 'brother', 'sister',
        'alumni', 'veteran', 'colleague', 'neighbor', 'believer'
    ]

    COMMITMENT_ESCALATION_PATTERNS = [
        ('small_request', ['quick survey', 'just one question', 'simple form']),
        ('medium_request', ['share your details', 'verify account', 'provide information']),
        ('large_request', ['wire transfer', 'full access', 'credentials', 'payment'])
    ]

    def __init__(self):
        self.interaction_history = {}

    def analyze_message(self, message: str, sender_info: Dict = None) -> List[TrustManipulationIndicator]:
        """
        Analyze a message for trust exploitation patterns.

        Args:
            message: The text content to analyze
            sender_info: Optional sender metadata
        """
        indicators = []
        message_lower = message.lower()

        # Check for authority impersonation
        authority_matches = [sig for sig in self.AUTHORITY_SIGNALS if sig in message_lower]
        if authority_matches:
            confidence = min(1.0, len(authority_matches) * 0.2)
            indicators.append(TrustManipulationIndicator(
                exploitation_type=TrustExploitationType.AUTHORITY_IMPERSONATION,
                confidence=confidence,
                evidence=authority_matches,
                risk_level='high' if confidence > 0.6 else 'medium'
            ))

        # Check for urgency pressure
        urgency_matches = [sig for sig in self.URGENCY_SIGNALS if sig in message_lower]
        if urgency_matches:
            confidence = min(1.0, len(urgency_matches) * 0.25)
            indicators.append(TrustManipulationIndicator(
                exploitation_type=TrustExploitationType.URGENCY_PRESSURE,
                confidence=confidence,
                evidence=urgency_matches,
                risk_level='high' if confidence > 0.5 else 'medium'
            ))

        # Check for reciprocity triggers
        reciprocity_matches = [sig for sig in self.RECIPROCITY_SIGNALS if sig in message_lower]
        if reciprocity_matches:
            confidence = min(1.0, len(reciprocity_matches) * 0.3)
            indicators.append(TrustManipulationIndicator(
                exploitation_type=TrustExploitationType.RECIPROCITY_TRIGGER,
                confidence=confidence,
                evidence=reciprocity_matches,
                risk_level='medium'
            ))

        # Check for affinity exploitation
        affinity_matches = [sig for sig in self.AFFINITY_SIGNALS if sig in message_lower]
        if affinity_matches:
            confidence = min(1.0, len(affinity_matches) * 0.25)
            indicators.append(TrustManipulationIndicator(
                exploitation_type=TrustExploitationType.AFFINITY_FRAUD,
                confidence=confidence,
                evidence=affinity_matches,
                risk_level='medium'
            ))

        # Combined pattern detection (more dangerous)
        if len(indicators) >= 2:
            # Multiple exploitation types = higher risk
            for indicator in indicators:
                indicator.risk_level = 'critical' if indicator.risk_level == 'high' else 'high'

        return indicators

    def analyze_conversation_sequence(self, messages: List[Dict]) -> Dict:
        """
        Analyze a sequence of messages for escalation patterns.

        Expected format: [{'sender': str, 'content': str, 'timestamp': float}]
        """
        analysis = {
            'escalation_detected': False,
            'grooming_indicators': [],
            'trust_building_phase': False,
            'exploitation_phase': False,
            'risk_progression': [],
            'overall_risk_score': 0.0
        }

        if len(messages) < 3:
            return analysis

        # Track request sizes over time
        request_sizes = []

        for msg in messages:
            content_lower = msg.get('content', '').lower()

            # Classify request size
            for size, patterns in self.COMMITMENT_ESCALATION_PATTERNS:
                if any(p in content_lower for p in patterns):
                    request_sizes.append(size)
                    break

        # Check for escalation pattern
        size_order = {'small_request': 1, 'medium_request': 2, 'large_request': 3}

        if len(request_sizes) >= 2:
            # Check if requests are escalating
            escalating = True
            for i in range(1, len(request_sizes)):
                if size_order.get(request_sizes[i], 0) <= size_order.get(request_sizes[i-1], 0):
                    escalating = False
                    break

            if escalating:
                analysis['escalation_detected'] = True
                analysis['grooming_indicators'].append('COMMITMENT_ESCALATION')
                analysis['overall_risk_score'] += 0.4

        # Analyze trust building phase
        early_messages = messages[:len(messages)//2]
        late_messages = messages[len(messages)//2:]

        early_risk = sum(len(self.analyze_message(m.get('content', ''))) for m in early_messages)
        late_risk = sum(len(self.analyze_message(m.get('content', ''))) for m in late_messages)

        if early_risk < late_risk:
            analysis['trust_building_phase'] = True
            analysis['exploitation_phase'] = True
            analysis['grooming_indicators'].append('TRUST_THEN_EXPLOIT_PATTERN')
            analysis['overall_risk_score'] += 0.3

        analysis['overall_risk_score'] = min(1.0, analysis['overall_risk_score'])

        return analysis


class GroomingPatternDetector:
    """
    Detects grooming behavior patterns in online interactions.

    Research basis:
    - Zero Abuse Project 2024: Manipulation, Grooming, and Gradual Desensitization
    - Research on predictable grooming stages
    """

    GROOMING_STAGES = {
        'selection': {
            'indicators': [
                'personal_questions', 'vulnerability_probing', 'isolation_attempts',
                'compliments_excessive', 'special_attention'
            ],
            'patterns': [
                r'tell me about yourself',
                r'do you have many friends',
                r'are you alone',
                r'you\'re (so |very )?(special|unique|different)',
                r'no one understands you like'
            ]
        },
        'trust_building': {
            'indicators': [
                'shared_secrets', 'exclusive_relationship', 'gift_giving',
                'reliability_demonstration', 'understanding_claims'
            ],
            'patterns': [
                r'just between us',
                r'our (little )?secret',
                r'i\'ll always be here',
                r'you can trust me',
                r'i understand you'
            ]
        },
        'desensitization': {
            'indicators': [
                'boundary_testing', 'normalization', 'gradual_exposure',
                'secrecy_requests', 'guilt_manipulation'
            ],
            'patterns': [
                r'everyone does',
                r'it\'s (normal|natural)',
                r'don\'t tell anyone',
                r'you (owe|promised) me',
                r'after everything i\'ve done'
            ]
        },
        'exploitation': {
            'indicators': [
                'explicit_requests', 'threats', 'blackmail',
                'isolation_complete', 'control_established'
            ],
            'patterns': [
                r'send me',
                r'if you don\'t',
                r'i\'ll tell everyone',
                r'no one will believe',
                r'you have no choice'
            ]
        }
    }

    def analyze_interaction_sequence(self, interactions: List[Dict]) -> GroomingStageAnalysis:
        """
        Analyze interaction sequence for grooming patterns.

        Expected format: [{'content': str, 'timestamp': float, 'sender': str}]
        """
        stage_scores = {stage: 0.0 for stage in self.GROOMING_STAGES}
        all_indicators = []

        for interaction in interactions:
            content = interaction.get('content', '').lower()

            for stage, stage_data in self.GROOMING_STAGES.items():
                for pattern in stage_data['patterns']:
                    if re.search(pattern, content):
                        stage_scores[stage] += 1
                        all_indicators.append(f"{stage}:{pattern}")

        # Determine dominant stage
        max_stage = max(stage_scores, key=stage_scores.get)
        max_score = stage_scores[max_stage]

        # Calculate progression velocity
        if len(interactions) >= 2:
            time_span = interactions[-1]['timestamp'] - interactions[0]['timestamp']
            velocity = sum(stage_scores.values()) / (time_span / 3600) if time_span > 0 else 0
        else:
            velocity = 0

        # Calculate risk score
        # Higher stages = higher risk, faster progression = higher risk
        stage_weights = {'selection': 0.2, 'trust_building': 0.4, 'desensitization': 0.7, 'exploitation': 1.0}
        risk_score = stage_weights.get(max_stage, 0) * min(1.0, max_score / 3)

        # Fast progression increases risk
        if velocity > 2:  # More than 2 indicators per hour
            risk_score = min(1.0, risk_score + 0.2)

        return GroomingStageAnalysis(
            stage=max_stage if max_score > 0 else 'none',
            indicators=all_indicators,
            progression_velocity=velocity,
            risk_score=risk_score
        )
```

---

## 4. PLATFORM-SPECIFIC MECHANICS

### Research Findings

**Gamification Dark Patterns:**
- Streaks exploit loss aversion (Kahneman's Prospect Theory): losing feels 2x worse than gaining
- Breaking streaks feels like "losing part of yourself" - identity attachment
- Variable ratio reinforcement = slot machine psychology
- Duolingo, Snapchat streaks create anxiety and compulsive behavior

**Notification Engineering:**
- FOMO-inducing notifications create urgency without substance
- Strategic timing to maximize engagement
- Batch notifications vs real-time = manipulation choice

**Infinite Scroll & Autoplay:**
- "Bottomless bowl" effect - no natural stopping cues
- Zeigarnik Effect: incomplete tasks remembered better
- Synergy with personalization creates "cognitive absorption"
- Time distortion reported by users

**Subscription Dark Patterns (CHI 2024 "Roach Motel"):**
- Signup: 1-2 clicks; Cancellation: 8+ minutes average
- Forced phone calls, typing confirmation phrases
- Visual interference: alternating button colors

```python
class GamificationManipulationType(Enum):
    STREAK_LOSS_AVERSION = "streak_punishment"
    VARIABLE_RATIO_REWARD = "slot_machine"
    SOCIAL_COMPARISON = "leaderboard_pressure"
    ARTIFICIAL_SCARCITY = "limited_availability"
    PROGRESS_ILLUSION = "fake_progress"
    FOMO_NOTIFICATION = "fear_of_missing_out"
    INFINITE_SCROLL = "bottomless_consumption"
    AUTOPLAY = "friction_removal"
    ROACH_MOTEL = "easy_in_hard_out"

@dataclass
class GamificationAnalysis:
    """Analysis of gamification manipulation"""
    manipulation_types: List[GamificationManipulationType] = field(default_factory=list)
    streak_dependency_score: float = 0.0
    variable_reward_frequency: float = 0.0
    friction_asymmetry: float = 0.0  # signup ease vs cancel difficulty
    overall_manipulation_score: float = 0.0
    detailed_findings: Dict = field(default_factory=dict)

class PlatformManipulationDetector:
    """
    Detects manipulation mechanics in platform/app design.

    Research basis:
    - CHI 2024: "Staying at the Roach Motel" subscription analysis
    - 2024 research on gamification dark patterns
    - Kahneman's Prospect Theory (loss aversion)
    - Wansink's "bottomless bowl" experiment
    """

    # Streak-related UI patterns
    STREAK_PATTERNS = {
        'visual_elements': ['fire', 'flame', 'chain', 'streak', 'consecutive', 'daily'],
        'loss_framing': ['don\'t lose', 'protect', 'maintain', 'keep alive', 'at risk'],
        'guilt_triggers': ['you\'ll lose', 'streak will end', 'don\'t break', 'miss out']
    }

    # Notification manipulation patterns
    NOTIFICATION_PATTERNS = {
        'fomo': ['someone just', 'you\'re missing', 'happening now', 'don\'t miss'],
        'false_urgency': ['limited time', 'expiring', 'last chance', 'ending soon'],
        'social_pressure': ['friends are', 'everyone is', 'you\'re falling behind'],
        'curiosity_gap': ['you won\'t believe', 'find out', 'see what', 'discover']
    }

    # Cancellation friction patterns
    CANCELLATION_FRICTION = {
        'required_call': 0.8,  # Must call to cancel
        'long_survey': 0.5,  # Forced feedback before cancel
        'confirmation_typing': 0.6,  # Must type phrase like "CONFIRM"
        'hidden_button': 0.4,  # Cancel button hard to find
        'emotional_manipulation': 0.7,  # "We'll miss you" guilt
        'multiple_screens': 0.5,  # Many steps to cancel
        'retention_offers': 0.3,  # Discount offers to stay
    }

    def __init__(self):
        self.thresholds = {
            'high_streak_dependency': 0.7,
            'frequent_variable_rewards': 0.5,
            'severe_friction_asymmetry': 0.6
        }

    def analyze_app_interface(self, interface_data: Dict) -> GamificationAnalysis:
        """
        Analyze app/platform interface for manipulation patterns.

        Expected interface_data:
        {
            'features': List[str],
            'notifications': List[Dict],
            'signup_steps': int,
            'cancel_steps': int,
            'cancel_requirements': List[str],
            'reward_schedule': str,  # 'fixed', 'variable', 'none'
            'ui_elements': List[Dict]
        }
        """
        analysis = GamificationAnalysis()

        # Analyze streak mechanics
        if 'features' in interface_data:
            features_lower = [f.lower() for f in interface_data['features']]

            streak_elements = sum(
                1 for pattern in self.STREAK_PATTERNS['visual_elements']
                if any(pattern in f for f in features_lower)
            )

            loss_framing = sum(
                1 for pattern in self.STREAK_PATTERNS['loss_framing']
                if any(pattern in f for f in features_lower)
            )

            if streak_elements > 0:
                analysis.manipulation_types.append(GamificationManipulationType.STREAK_LOSS_AVERSION)
                analysis.streak_dependency_score = min(1.0, (streak_elements + loss_framing * 2) * 0.2)

        # Analyze reward schedule
        if interface_data.get('reward_schedule') == 'variable':
            analysis.manipulation_types.append(GamificationManipulationType.VARIABLE_RATIO_REWARD)
            analysis.variable_reward_frequency = 0.7  # High manipulation potential

        # Analyze friction asymmetry (roach motel)
        signup_steps = interface_data.get('signup_steps', 1)
        cancel_steps = interface_data.get('cancel_steps', 1)

        if cancel_steps > signup_steps:
            analysis.friction_asymmetry = min(1.0, (cancel_steps - signup_steps) / 10)

            if analysis.friction_asymmetry > 0.3:
                analysis.manipulation_types.append(GamificationManipulationType.ROACH_MOTEL)

        # Analyze cancellation requirements
        if 'cancel_requirements' in interface_data:
            friction_score = 0
            for req in interface_data['cancel_requirements']:
                req_lower = req.lower()
                for friction_type, score in self.CANCELLATION_FRICTION.items():
                    if friction_type.replace('_', ' ') in req_lower:
                        friction_score += score

            analysis.friction_asymmetry = max(analysis.friction_asymmetry, min(1.0, friction_score))

        # Analyze notifications
        if 'notifications' in interface_data:
            notification_analysis = self._analyze_notifications(interface_data['notifications'])
            analysis.detailed_findings['notifications'] = notification_analysis

            if notification_analysis.get('fomo_count', 0) > 0:
                analysis.manipulation_types.append(GamificationManipulationType.FOMO_NOTIFICATION)

        # Check for infinite scroll / autoplay
        if 'features' in interface_data:
            if any('infinite' in f.lower() or 'endless' in f.lower() for f in interface_data['features']):
                analysis.manipulation_types.append(GamificationManipulationType.INFINITE_SCROLL)

            if any('autoplay' in f.lower() or 'auto-play' in f.lower() for f in interface_data['features']):
                analysis.manipulation_types.append(GamificationManipulationType.AUTOPLAY)

        # Calculate overall manipulation score
        analysis.overall_manipulation_score = min(1.0,
            len(analysis.manipulation_types) * 0.15 +
            analysis.streak_dependency_score * 0.25 +
            analysis.variable_reward_frequency * 0.3 +
            analysis.friction_asymmetry * 0.3
        )

        return analysis

    def _analyze_notifications(self, notifications: List[Dict]) -> Dict:
        """Analyze notification patterns for manipulation"""
        analysis = {
            'total': len(notifications),
            'fomo_count': 0,
            'false_urgency_count': 0,
            'social_pressure_count': 0,
            'curiosity_gap_count': 0,
            'manipulation_rate': 0.0
        }

        for notif in notifications:
            content = notif.get('content', '').lower()

            for pattern in self.NOTIFICATION_PATTERNS['fomo']:
                if pattern in content:
                    analysis['fomo_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['false_urgency']:
                if pattern in content:
                    analysis['false_urgency_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['social_pressure']:
                if pattern in content:
                    analysis['social_pressure_count'] += 1
                    break

            for pattern in self.NOTIFICATION_PATTERNS['curiosity_gap']:
                if pattern in content:
                    analysis['curiosity_gap_count'] += 1
                    break

        manipulative_count = (
            analysis['fomo_count'] +
            analysis['false_urgency_count'] +
            analysis['social_pressure_count'] +
            analysis['curiosity_gap_count']
        )

        analysis['manipulation_rate'] = manipulative_count / len(notifications) if notifications else 0

        return analysis


class InfiniteScrollDetector:
    """
    Detects infinite scroll and attention capture patterns.

    Research basis:
    - 2024 CHI: Design Frictions on Social Media
    - Wansink's bottomless bowl research
    - Zeigarnik Effect: incomplete tasks remembered better
    """

    def __init__(self):
        self.session_data = []

    def analyze_browsing_session(self, session_data: Dict) -> Dict:
        """
        Analyze browsing session for attention capture patterns.

        Expected session_data:
        {
            'scroll_events': [{'timestamp': float, 'position': float}],
            'content_views': [{'timestamp': float, 'duration': float, 'content_id': str}],
            'session_duration': float,
            'natural_endpoints': int,  # Number of clear stopping points
            'autoplay_triggers': int
        }
        """
        analysis = {
            'scroll_immersion_score': 0.0,
            'time_distortion_indicators': [],
            'stopping_point_deprivation': 0.0,
            'attention_capture_score': 0.0,
            'recommendations': []
        }

        scroll_events = session_data.get('scroll_events', [])
        content_views = session_data.get('content_views', [])
        duration = session_data.get('session_duration', 0)

        if scroll_events:
            # Calculate scroll velocity patterns
            velocities = []
            for i in range(1, len(scroll_events)):
                time_diff = scroll_events[i]['timestamp'] - scroll_events[i-1]['timestamp']
                pos_diff = abs(scroll_events[i]['position'] - scroll_events[i-1]['position'])
                if time_diff > 0:
                    velocities.append(pos_diff / time_diff)

            if velocities:
                # High consistent velocity = mindless scrolling
                avg_velocity = np.mean(velocities)
                velocity_consistency = 1 - (np.std(velocities) / avg_velocity if avg_velocity > 0 else 0)

                if velocity_consistency > 0.7:
                    analysis['scroll_immersion_score'] = velocity_consistency
                    analysis['time_distortion_indicators'].append('CONSISTENT_MINDLESS_SCROLLING')

        # Analyze content view patterns
        if content_views:
            view_durations = [v['duration'] for v in content_views]
            avg_duration = np.mean(view_durations)

            # Short average views = rapid consumption
            if avg_duration < 3:  # Less than 3 seconds per content
                analysis['time_distortion_indicators'].append('RAPID_CONTENT_CONSUMPTION')
                analysis['attention_capture_score'] += 0.3

        # Analyze natural endpoint deprivation
        natural_endpoints = session_data.get('natural_endpoints', 0)
        if duration > 0 and natural_endpoints > 0:
            endpoints_per_minute = natural_endpoints / (duration / 60)

            if endpoints_per_minute < 0.5:  # Less than 1 endpoint per 2 minutes
                analysis['stopping_point_deprivation'] = 1 - (endpoints_per_minute * 2)
                analysis['time_distortion_indicators'].append('NATURAL_STOPPING_POINTS_ABSENT')

        # Check autoplay contribution
        autoplay_triggers = session_data.get('autoplay_triggers', 0)
        if autoplay_triggers > 5:
            analysis['attention_capture_score'] += 0.3
            analysis['time_distortion_indicators'].append('EXCESSIVE_AUTOPLAY')

        # Final score calculation
        analysis['attention_capture_score'] = min(1.0,
            analysis['scroll_immersion_score'] * 0.3 +
            analysis['stopping_point_deprivation'] * 0.4 +
            analysis['attention_capture_score']
        )

        # Generate recommendations
        if analysis['attention_capture_score'] > 0.5:
            analysis['recommendations'].extend([
                'Consider enabling screen time limits',
                'Look for apps with natural stopping points',
                'Disable autoplay features where possible'
            ])

        return analysis
```

---

## 5. PHYSIOLOGICAL VALIDATION METHODS

### Research Findings

**Eye Tracking & Pupil Dilation:**
- Pupil dilation indicates cognitive load and emotional arousal
- 15% pupil dilation = reduced critical engagement
- EyeLink detects 0.1% pupil diameter changes
- Guilty knowledge detection: 70% accuracy via pupillary response
- Gaze patterns reveal deception in sender-receiver games

**Blink Rate:**
- Normal: 15-20 blinks/min
- Focused engagement: <10 blinks/min
- Elevated arousal: 30-45 blinks/min

**Skin Conductance (GSR):**
- 2-5 microsiemens = elevated arousal
- Indicates emotional response regardless of valence

**Heart Rate Variability (HRV):**
- <40ms = stress/anger state
- Normal: 50-100ms

```python
@dataclass
class PhysiologicalReading:
    """Single physiological measurement"""
    timestamp: float
    pupil_diameter: float = 0.0  # mm
    blink_rate: float = 0.0  # per minute
    gsr: float = 0.0  # microsiemens
    hrv: float = 0.0  # ms
    gaze_x: float = 0.0
    gaze_y: float = 0.0
    fixation_duration: float = 0.0  # ms

@dataclass
class PhysiologicalState:
    """Interpreted physiological state"""
    arousal_level: float = 0.0  # 0-1
    cognitive_load: float = 0.0  # 0-1
    emotional_valence: float = 0.0  # -1 to 1
    critical_engagement: float = 0.0  # 0-1 (low = vulnerable)
    stress_level: float = 0.0  # 0-1
    state_label: str = ""  # e.g., "vulnerable", "engaged", "stressed"

class PhysiologicalManipulationDetector:
    """
    Detects manipulation effects via physiological signals.

    Research basis:
    - PMC: Technological advancements in Neuromarketing
    - SR Research: Pupillometry research applications
    - PNAS Nexus 2024: Phishing vulnerability and cognition
    - EEG research on video editing effects
    """

    # Thresholds from APPENDIX_RESEARCH_SOURCES.md
    THRESHOLDS = {
        'blink_rate_normal_low': 15,
        'blink_rate_normal_high': 20,
        'blink_rate_focused': 10,  # Below this = high focus
        'blink_rate_aroused': 30,  # Above this = elevated arousal
        'gsr_baseline': 1.0,
        'gsr_elevated': 2.0,  # Above this = aroused
        'gsr_high': 5.0,
        'hrv_stress': 40,  # Below this = stressed
        'hrv_normal_low': 50,
        'hrv_normal_high': 100,
        'pupil_baseline': 1.0,  # Ratio to baseline
        'pupil_reduced_critical': 1.15,  # Above this = reduced critical thinking
    }

    def __init__(self):
        self.baseline_readings = None

    def set_baseline(self, readings: List[PhysiologicalReading]):
        """Establish baseline from calm state readings"""
        if readings:
            self.baseline_readings = {
                'pupil': np.mean([r.pupil_diameter for r in readings]),
                'blink_rate': np.mean([r.blink_rate for r in readings]),
                'gsr': np.mean([r.gsr for r in readings]),
                'hrv': np.mean([r.hrv for r in readings])
            }

    def analyze_reading(self, reading: PhysiologicalReading) -> PhysiologicalState:
        """Analyze single reading against baseline and thresholds"""
        state = PhysiologicalState()

        # Use baseline if available, otherwise use absolute thresholds
        baseline = self.baseline_readings or {
            'pupil': 4.0,  # Average pupil diameter mm
            'blink_rate': 17.5,
            'gsr': 1.0,
            'hrv': 75
        }

        # Pupil dilation analysis
        if baseline['pupil'] > 0:
            pupil_ratio = reading.pupil_diameter / baseline['pupil']

            # High dilation = emotional arousal, potentially reduced critical thinking
            if pupil_ratio > self.THRESHOLDS['pupil_reduced_critical']:
                state.critical_engagement = max(0, 1 - (pupil_ratio - 1) * 2)
                state.arousal_level = min(1.0, (pupil_ratio - 1) * 3)
            else:
                state.critical_engagement = 1.0
                state.arousal_level = max(0, (pupil_ratio - 0.9) * 5)

        # Blink rate analysis
        if reading.blink_rate < self.THRESHOLDS['blink_rate_focused']:
            # Very low blink rate = high focus, potentially hypnotic state
            state.cognitive_load = 0.8
            state.state_label = "hyperfocused"
        elif reading.blink_rate > self.THRESHOLDS['blink_rate_aroused']:
            # High blink rate = arousal, stress, or threat response
            state.arousal_level = min(1.0, state.arousal_level + 0.3)
            state.stress_level = min(1.0, (reading.blink_rate - 30) / 15)
            state.state_label = "aroused"

        # GSR analysis
        if reading.gsr > self.THRESHOLDS['gsr_elevated']:
            state.arousal_level = min(1.0, state.arousal_level +
                (reading.gsr - self.THRESHOLDS['gsr_baseline']) / 4)

            if reading.gsr > self.THRESHOLDS['gsr_high']:
                state.state_label = "highly_aroused"

        # HRV analysis
        if reading.hrv < self.THRESHOLDS['hrv_stress']:
            state.stress_level = min(1.0, state.stress_level +
                (self.THRESHOLDS['hrv_stress'] - reading.hrv) / 40)
            state.state_label = "stressed"

        # Determine vulnerability state
        if state.critical_engagement < 0.5 and state.arousal_level > 0.6:
            state.state_label = "vulnerable"

        return state

    def detect_manipulation_response(
        self,
        pre_exposure: List[PhysiologicalReading],
        during_exposure: List[PhysiologicalReading],
        content_type: str = ""
    ) -> Dict:
        """
        Detect physiological response to potential manipulation.

        Compares pre-exposure baseline to during-exposure readings.
        """
        analysis = {
            'manipulation_detected': False,
            'response_type': '',
            'intensity': 0.0,
            'vulnerability_window': [],
            'recovery_needed': False,
            'detailed_changes': {}
        }

        if not pre_exposure or not during_exposure:
            return analysis

        # Calculate baseline
        pre_avg = {
            'pupil': np.mean([r.pupil_diameter for r in pre_exposure]),
            'blink': np.mean([r.blink_rate for r in pre_exposure]),
            'gsr': np.mean([r.gsr for r in pre_exposure]),
            'hrv': np.mean([r.hrv for r in pre_exposure])
        }

        # Calculate during exposure
        during_avg = {
            'pupil': np.mean([r.pupil_diameter for r in during_exposure]),
            'blink': np.mean([r.blink_rate for r in during_exposure]),
            'gsr': np.mean([r.gsr for r in during_exposure]),
            'hrv': np.mean([r.hrv for r in during_exposure])
        }

        # Calculate changes
        changes = {
            'pupil_change': (during_avg['pupil'] - pre_avg['pupil']) / pre_avg['pupil'] if pre_avg['pupil'] > 0 else 0,
            'blink_change': during_avg['blink'] - pre_avg['blink'],
            'gsr_change': during_avg['gsr'] - pre_avg['gsr'],
            'hrv_change': during_avg['hrv'] - pre_avg['hrv']
        }

        analysis['detailed_changes'] = changes

        # Detect manipulation patterns

        # Pattern 1: Fear/Threat response (dilated pupils, high GSR, low HRV)
        if (changes['pupil_change'] > 0.1 and
            changes['gsr_change'] > 1.0 and
            changes['hrv_change'] < -10):
            analysis['manipulation_detected'] = True
            analysis['response_type'] = 'fear_threat'
            analysis['intensity'] = min(1.0, changes['gsr_change'] / 3)

        # Pattern 2: Hypnotic engagement (reduced blink, stable pupil)
        elif changes['blink_change'] < -5 and abs(changes['pupil_change']) < 0.05:
            analysis['manipulation_detected'] = True
            analysis['response_type'] = 'hypnotic_engagement'
            analysis['intensity'] = min(1.0, abs(changes['blink_change']) / 10)

        # Pattern 3: Emotional arousal (high pupil dilation, high GSR)
        elif changes['pupil_change'] > 0.15 and changes['gsr_change'] > 1.5:
            analysis['manipulation_detected'] = True
            analysis['response_type'] = 'emotional_arousal'
            analysis['intensity'] = min(1.0, changes['pupil_change'] * 3)

        # Pattern 4: Stress/pressure (low HRV, high blink rate, high GSR)
        elif (changes['hrv_change'] < -15 and
              changes['blink_change'] > 10 and
              changes['gsr_change'] > 1.0):
            analysis['manipulation_detected'] = True
            analysis['response_type'] = 'stress_pressure'
            analysis['intensity'] = min(1.0, abs(changes['hrv_change']) / 30)

        # Identify vulnerability windows
        for i, reading in enumerate(during_exposure):
            state = self.analyze_reading(reading)
            if state.critical_engagement < 0.5:
                analysis['vulnerability_window'].append({
                    'index': i,
                    'timestamp': reading.timestamp,
                    'critical_engagement': state.critical_engagement
                })

        # Determine if recovery is needed
        if analysis['intensity'] > 0.6 or len(analysis['vulnerability_window']) > len(during_exposure) * 0.5:
            analysis['recovery_needed'] = True

        return analysis


class GazePatternAnalyzer:
    """
    Analyzes gaze patterns for manipulation indicators.

    Research basis:
    - Pinocchio's Pupil: Eyetracking and deception detection
    - 2024: Gaze patterns in sender-receiver games
    """

    def __init__(self):
        self.aoi_definitions = {}  # Areas of interest

    def define_aoi(self, name: str, bounds: Tuple[float, float, float, float]):
        """Define area of interest (x_min, y_min, x_max, y_max)"""
        self.aoi_definitions[name] = bounds

    def analyze_gaze_sequence(
        self,
        gaze_data: List[Dict],
        content_regions: Dict[str, Tuple]
    ) -> Dict:
        """
        Analyze gaze sequence for attention manipulation patterns.

        Expected gaze_data: [{'x': float, 'y': float, 'timestamp': float, 'duration': float}]
        content_regions: {'cta_button': (x, y, w, h), 'price': (x, y, w, h), ...}
        """
        analysis = {
            'attention_distribution': {},
            'manipulation_indicators': [],
            'dwell_time_analysis': {},
            'scanpath_pattern': '',
            'attention_capture_effectiveness': 0.0
        }

        if not gaze_data:
            return analysis

        # Calculate dwell time per region
        region_dwell = {region: 0 for region in content_regions}
        total_dwell = 0

        for gaze in gaze_data:
            x, y = gaze.get('x', 0), gaze.get('y', 0)
            duration = gaze.get('duration', 0)
            total_dwell += duration

            for region, bounds in content_regions.items():
                rx, ry, rw, rh = bounds
                if rx <= x <= rx + rw and ry <= y <= ry + rh:
                    region_dwell[region] += duration
                    break

        # Calculate attention distribution
        if total_dwell > 0:
            analysis['attention_distribution'] = {
                region: dwell / total_dwell
                for region, dwell in region_dwell.items()
            }

        # Detect manipulation patterns

        # Pattern 1: Disproportionate CTA attention
        if 'cta_button' in analysis['attention_distribution']:
            cta_attention = analysis['attention_distribution']['cta_button']
            if cta_attention > 0.3:  # More than 30% on CTA
                analysis['manipulation_indicators'].append('HIGH_CTA_ATTENTION')

        # Pattern 2: Price avoidance (manipulation redirecting from price)
        if 'price' in analysis['attention_distribution']:
            price_attention = analysis['attention_distribution']['price']
            if price_attention < 0.05:  # Less than 5% on price
                analysis['manipulation_indicators'].append('PRICE_ATTENTION_SUPPRESSED')

        # Pattern 3: Scanpath analysis (F-pattern vs manipulated pattern)
        analysis['scanpath_pattern'] = self._classify_scanpath(gaze_data)

        if analysis['scanpath_pattern'] == 'linear_forced':
            analysis['manipulation_indicators'].append('FORCED_ATTENTION_PATH')

        # Calculate attention capture effectiveness
        cta_regions = [r for r in content_regions if 'cta' in r.lower() or 'button' in r.lower()]
        cta_attention = sum(analysis['attention_distribution'].get(r, 0) for r in cta_regions)

        analysis['attention_capture_effectiveness'] = min(1.0, cta_attention * 2)

        return analysis

    def _classify_scanpath(self, gaze_data: List[Dict]) -> str:
        """Classify the scanpath pattern"""
        if len(gaze_data) < 5:
            return 'insufficient_data'

        # Extract x, y sequences
        xs = [g['x'] for g in gaze_data]
        ys = [g['y'] for g in gaze_data]

        # Check for F-pattern (natural reading)
        # Starts top-left, moves right, drops down, moves right again
        if xs[0] < np.mean(xs) and ys[0] < np.mean(ys):
            horizontal_moves = sum(1 for i in range(1, len(xs)) if xs[i] > xs[i-1])
            if horizontal_moves > len(xs) * 0.4:
                return 'f_pattern_natural'

        # Check for linear forced pattern
        # Very consistent direction, limited exploration
        x_direction = np.sign(np.diff(xs))
        y_direction = np.sign(np.diff(ys))

        if np.std(x_direction) < 0.5 or np.std(y_direction) < 0.5:
            return 'linear_forced'

        # Check for scattered pattern
        if np.std(xs) > np.mean(xs) * 0.5 and np.std(ys) > np.mean(ys) * 0.5:
            return 'scattered'

        return 'mixed'
```

---

## 6. VULNERABLE POPULATION DETECTION

### Research Findings

**Children & Adolescents:**
- 25% of 8-year-olds have experienced online harm (2024)
- 33% of boys 9-12 experienced harmful online sexual interaction (2024)
- Cannot comprehend persuasive intent of advertising
- Developing prefrontal cortex = limited impulse control

**Elderly:**
- $3.1 billion lost to cyber fraud in 2022 (74% increase from 2021)
- Mild cognitive decline correlates with higher scam vulnerability
- APOE4 gene variant increases phishing vulnerability
- Entorhinal cortex thinning linked to financial exploitation
- Social isolation is strongest risk factor

**Neurodivergent:**
- ADHD/Autism more vulnerable to narcissistic manipulation
- Difficulty recognizing manipulative social cues
- More susceptible to gaslighting
- Late/undiagnosed individuals especially vulnerable
- Low self-esteem from chronic invalidation

```python
class VulnerabilityFactorType(Enum):
    AGE_CHILD = "child_developing_cognition"
    AGE_ADOLESCENT = "adolescent_risk_taking"
    AGE_ELDERLY = "elderly_cognitive_decline"
    COGNITIVE_LOAD = "high_cognitive_load"
    EMOTIONAL_STATE = "vulnerable_emotional_state"
    SOCIAL_ISOLATION = "isolated_lonely"
    NEURODIVERGENT = "neurodivergent_processing"
    MENTAL_HEALTH = "mental_health_condition"
    DIGITAL_LITERACY = "low_digital_literacy"
    FINANCIAL_STRESS = "financial_vulnerability"

@dataclass
class VulnerabilityProfile:
    """Individual vulnerability assessment"""
    factors: List[VulnerabilityFactorType] = field(default_factory=list)
    overall_vulnerability_score: float = 0.0
    exploitation_risk_areas: List[str] = field(default_factory=list)
    protective_recommendations: List[str] = field(default_factory=list)
    requires_enhanced_protection: bool = False

class VulnerablePopulationDetector:
    """
    Detects and assesses vulnerability to manipulation.

    Research basis:
    - USC Dornsife 2024: Alzheimer's and financial scam vulnerability
    - PNAS Nexus 2024: APOE4 genotype and phishing vulnerability
    - Thorn 2024: Youth online sexual interaction data
    - Frontiers 2024: Digital media in early childhood
    - Psychology Today 2025: Neurodivergent manipulation vulnerability
    """

    # Age-based vulnerability factors
    AGE_VULNERABILITY = {
        'child': {
            'age_range': (0, 12),
            'base_vulnerability': 0.8,
            'factors': [
                'Cannot comprehend persuasive intent',
                'Limited critical evaluation skills',
                'High trust in perceived authorities',
                'Difficulty distinguishing ads from content'
            ]
        },
        'adolescent': {
            'age_range': (13, 17),
            'base_vulnerability': 0.6,
            'factors': [
                'Developing prefrontal cortex',
                'Heightened social comparison',
                'Risk-taking behavior',
                'FOMO susceptibility',
                'Identity formation vulnerability'
            ]
        },
        'young_adult': {
            'age_range': (18, 25),
            'base_vulnerability': 0.3,
            'factors': [
                'Still developing impulse control',
                'Social media native',
                'Financial inexperience'
            ]
        },
        'adult': {
            'age_range': (26, 64),
            'base_vulnerability': 0.2,
            'factors': [
                'Work stress vulnerability',
                'Family responsibility pressure'
            ]
        },
        'elderly': {
            'age_range': (65, 120),
            'base_vulnerability': 0.5,
            'factors': [
                'Potential cognitive decline',
                'Social isolation risk',
                'Digital literacy gaps',
                'Trust in authority',
                'Limited fraud recovery time'
            ]
        }
    }

    # Cognitive indicators of vulnerability
    COGNITIVE_VULNERABILITY_INDICATORS = {
        'processing_speed_decline': 0.3,
        'memory_issues': 0.4,
        'decision_fatigue': 0.3,
        'attention_difficulties': 0.3,
        'executive_function_issues': 0.4
    }

    # Emotional state vulnerability multipliers
    EMOTIONAL_VULNERABILITY_MULTIPLIERS = {
        'depression': 1.5,
        'anxiety': 1.4,
        'loneliness': 1.6,
        'grief': 1.5,
        'stress': 1.3,
        'excitement': 1.2,  # Can impair judgment
        'fear': 1.4
    }

    def __init__(self):
        self.population_baselines = {}

    def assess_individual_vulnerability(self, user_data: Dict) -> VulnerabilityProfile:
        """
        Assess individual vulnerability to manipulation.

        Expected user_data:
        {
            'age': int,
            'cognitive_indicators': List[str],
            'emotional_state': str,
            'social_connection_score': float,  # 0-1, higher = more connected
            'digital_literacy_score': float,  # 0-1, higher = more literate
            'neurodivergent_flags': List[str],
            'financial_stress': bool,
            'recent_life_events': List[str]
        }
        """
        profile = VulnerabilityProfile()
        vulnerability_score = 0.0

        # Age-based assessment
        age = user_data.get('age', 30)
        for category, data in self.AGE_VULNERABILITY.items():
            if data['age_range'][0] <= age <= data['age_range'][1]:
                vulnerability_score += data['base_vulnerability']

                if category == 'child':
                    profile.factors.append(VulnerabilityFactorType.AGE_CHILD)
                    profile.exploitation_risk_areas.extend([
                        'In-app purchases', 'Advertising', 'Data collection',
                        'Contact from strangers', 'Inappropriate content'
                    ])
                    profile.requires_enhanced_protection = True

                elif category == 'adolescent':
                    profile.factors.append(VulnerabilityFactorType.AGE_ADOLESCENT)
                    profile.exploitation_risk_areas.extend([
                        'Social comparison manipulation', 'FOMO tactics',
                        'Influencer marketing', 'Dating app manipulation',
                        'Sextortion risk'
                    ])

                elif category == 'elderly':
                    profile.factors.append(VulnerabilityFactorType.AGE_ELDERLY)
                    profile.exploitation_risk_areas.extend([
                        'Tech support scams', 'Romance scams',
                        'Phishing', 'Investment fraud',
                        'Grandparent scams'
                    ])

                break

        # Cognitive vulnerability assessment
        cognitive_indicators = user_data.get('cognitive_indicators', [])
        for indicator in cognitive_indicators:
            if indicator in self.COGNITIVE_VULNERABILITY_INDICATORS:
                vulnerability_score += self.COGNITIVE_VULNERABILITY_INDICATORS[indicator]
                profile.factors.append(VulnerabilityFactorType.COGNITIVE_LOAD)

        # Emotional state assessment
        emotional_state = user_data.get('emotional_state', '')
        if emotional_state in self.EMOTIONAL_VULNERABILITY_MULTIPLIERS:
            multiplier = self.EMOTIONAL_VULNERABILITY_MULTIPLIERS[emotional_state]
            vulnerability_score *= multiplier
            profile.factors.append(VulnerabilityFactorType.EMOTIONAL_STATE)
            profile.exploitation_risk_areas.append(f'Exploitation during {emotional_state}')

        # Social connection assessment
        social_score = user_data.get('social_connection_score', 0.5)
        if social_score < 0.3:
            vulnerability_score += 0.3
            profile.factors.append(VulnerabilityFactorType.SOCIAL_ISOLATION)
            profile.exploitation_risk_areas.append('Romance scams')
            profile.exploitation_risk_areas.append('Companionship manipulation')

        # Digital literacy assessment
        digital_literacy = user_data.get('digital_literacy_score', 0.5)
        if digital_literacy < 0.4:
            vulnerability_score += 0.3
            profile.factors.append(VulnerabilityFactorType.DIGITAL_LITERACY)
            profile.exploitation_risk_areas.append('Phishing')
            profile.exploitation_risk_areas.append('Malware')
            profile.exploitation_risk_areas.append('Tech support scams')

        # Neurodivergent assessment
        nd_flags = user_data.get('neurodivergent_flags', [])
        if nd_flags:
            vulnerability_score += 0.2
            profile.factors.append(VulnerabilityFactorType.NEURODIVERGENT)
            profile.exploitation_risk_areas.extend([
                'Gaslighting', 'Social manipulation',
                'Boundary violations', 'Coercive control'
            ])

        # Financial stress assessment
        if user_data.get('financial_stress', False):
            vulnerability_score += 0.25
            profile.factors.append(VulnerabilityFactorType.FINANCIAL_STRESS)
            profile.exploitation_risk_areas.extend([
                'Get-rich-quick schemes', 'Loan scams',
                'Predatory lending', 'Advance fee fraud'
            ])

        # Normalize score
        profile.overall_vulnerability_score = min(1.0, vulnerability_score)

        # Determine if enhanced protection needed
        if profile.overall_vulnerability_score > 0.7:
            profile.requires_enhanced_protection = True

        # Generate recommendations
        profile.protective_recommendations = self._generate_recommendations(profile)

        return profile

    def _generate_recommendations(self, profile: VulnerabilityProfile) -> List[str]:
        """Generate protective recommendations based on vulnerability profile"""
        recommendations = []

        if VulnerabilityFactorType.AGE_CHILD in profile.factors:
            recommendations.extend([
                'Enable parental controls on all devices',
                'Use child-safe apps and browsers',
                'Discuss online safety regularly',
                'Monitor online activity',
                'Disable in-app purchases'
            ])

        if VulnerabilityFactorType.AGE_ELDERLY in profile.factors:
            recommendations.extend([
                'Set up call blocking for unknown numbers',
                'Establish a trusted contact for financial decisions',
                'Use password managers with family sharing',
                'Enable multi-factor authentication',
                'Participate in fraud prevention education'
            ])

        if VulnerabilityFactorType.SOCIAL_ISOLATION in profile.factors:
            recommendations.extend([
                'Be cautious of unsolicited contact',
                'Verify identities before sharing personal info',
                'Discuss major decisions with trusted friends/family',
                'Join legitimate community groups for connection'
            ])

        if VulnerabilityFactorType.NEURODIVERGENT in profile.factors:
            recommendations.extend([
                'Take time before making decisions under pressure',
                'Have a trusted person review major commitments',
                'Be aware of manipulation tactics',
                'Trust your instincts about uncomfortable situations'
            ])

        if VulnerabilityFactorType.EMOTIONAL_STATE in profile.factors:
            recommendations.extend([
                'Avoid major decisions when emotionally distressed',
                'Be extra cautious of urgency tactics',
                'Implement cooling-off periods for purchases',
                'Seek support before responding to pressure'
            ])

        return recommendations


class ChildSafetyDetector:
    """
    Specialized detection for child-targeted manipulation.

    Research basis:
    - Frontiers 2024: Digital media in early childhood
    - Thorn 2024: Youth online sexual interaction data
    - EU Parliament: Social media influence on children
    """

    # Patterns that indicate child-targeted manipulation
    CHILD_TARGETING_PATTERNS = {
        'visual_elements': [
            'cartoon', 'animated', 'colorful', 'character', 'mascot',
            'game', 'play', 'fun', 'adventure', 'magic'
        ],
        'language_patterns': [
            'kids', 'children', 'young', 'learn', 'educational',
            'family', 'safe', 'friendly'
        ],
        'manipulation_tactics': [
            'collect', 'unlock', 'level up', 'surprise', 'mystery',
            'limited edition', 'exclusive', 'special'
        ]
    }

    # Grooming language patterns (from research)
    GROOMING_LANGUAGE = {
        'selection_phase': [
            r'how old are you',
            r'do you have (a )?(boyfriend|girlfriend)',
            r'are your parents (home|around)',
            r'do you have (snapchat|instagram|tiktok)'
        ],
        'trust_building': [
            r'you\'re (so )?(mature|special|different)',
            r'i understand you',
            r'no one (else )?gets you',
            r'our (little )?secret'
        ],
        'isolation': [
            r'don\'t tell (anyone|your parents)',
            r'they wouldn\'t understand',
            r'just between us',
            r'private (chat|message)'
        ]
    }

    def analyze_content_for_child_targeting(self, content: Dict) -> Dict:
        """
        Analyze content for child-targeted manipulation.

        Expected content:
        {
            'text': str,
            'visual_elements': List[str],
            'audio_elements': List[str],
            'interactive_elements': List[str]
        }
        """
        analysis = {
            'child_targeted': False,
            'targeting_score': 0.0,
            'manipulation_tactics': [],
            'risk_level': 'low',
            'concerns': []
        }

        text = content.get('text', '').lower()
        visuals = [v.lower() for v in content.get('visual_elements', [])]

        # Check visual targeting
        visual_matches = sum(
            1 for pattern in self.CHILD_TARGETING_PATTERNS['visual_elements']
            if any(pattern in v for v in visuals)
        )

        # Check language targeting
        language_matches = sum(
            1 for pattern in self.CHILD_TARGETING_PATTERNS['language_patterns']
            if pattern in text
        )

        # Check manipulation tactics
        tactic_matches = []
        for tactic in self.CHILD_TARGETING_PATTERNS['manipulation_tactics']:
            if tactic in text:
                tactic_matches.append(tactic)

        # Calculate targeting score
        analysis['targeting_score'] = min(1.0,
            (visual_matches * 0.15) +
            (language_matches * 0.1) +
            (len(tactic_matches) * 0.2)
        )

        analysis['child_targeted'] = analysis['targeting_score'] > 0.3
        analysis['manipulation_tactics'] = tactic_matches

        # Assess risk level
        if analysis['targeting_score'] > 0.7:
            analysis['risk_level'] = 'high'
            analysis['concerns'].append('Heavy use of child-targeting manipulation')
        elif analysis['targeting_score'] > 0.4:
            analysis['risk_level'] = 'medium'
            analysis['concerns'].append('Moderate child-targeting elements')

        # Check for dark patterns in children's content
        if 'collect' in tactic_matches and 'limited' in text:
            analysis['concerns'].append('Artificial scarcity targeting children')

        if 'surprise' in tactic_matches or 'mystery' in tactic_matches:
            analysis['concerns'].append('Variable reward mechanics (gambling-like)')

        return analysis

    def detect_grooming_patterns(self, messages: List[Dict]) -> Dict:
        """
        Detect potential grooming patterns in message sequences.

        Expected messages: [{'sender': str, 'content': str, 'timestamp': float}]
        """
        analysis = {
            'grooming_detected': False,
            'phase': 'none',
            'confidence': 0.0,
            'matched_patterns': [],
            'risk_level': 'none',
            'immediate_action_needed': False
        }

        phase_scores = {phase: 0 for phase in self.GROOMING_LANGUAGE}

        for msg in messages:
            content = msg.get('content', '').lower()

            for phase, patterns in self.GROOMING_LANGUAGE.items():
                for pattern in patterns:
                    if re.search(pattern, content):
                        phase_scores[phase] += 1
                        analysis['matched_patterns'].append({
                            'phase': phase,
                            'pattern': pattern,
                            'content': content[:100]
                        })

        # Determine dominant phase
        max_phase = max(phase_scores, key=phase_scores.get)
        max_score = phase_scores[max_phase]

        if max_score > 0:
            analysis['phase'] = max_phase
            analysis['confidence'] = min(1.0, max_score / 3)

            # Progressive phases indicate active grooming
            phases_present = [p for p, s in phase_scores.items() if s > 0]

            if len(phases_present) >= 2:
                analysis['grooming_detected'] = True
                analysis['risk_level'] = 'high'

                if 'isolation' in phases_present:
                    analysis['risk_level'] = 'critical'
                    analysis['immediate_action_needed'] = True

            elif max_score >= 2:
                analysis['grooming_detected'] = True
                analysis['risk_level'] = 'medium'

        return analysis
```

---

## 7. ECONOMIC MANIPULATION MECHANICS

### Research Findings

**Dynamic Pricing (2024):**
- Amazon changes prices 2.5 million times per day
- "Surveillance pricing" uses personal data for individualized prices
- FTC investigating in July 2024
- Loyal customers often charged MORE
- Personalized pricing can increase profits 19%

**Anchoring & Decoy Effects:**
- 70% of consumers influenced by initial price anchor
- Williams-Sonoma: $429 decoy increased $275 model sales
- Campbell's "Limit 12" increased purchases from 3.3 to 7 cans
- Decoy pricing steers choices toward target option

**Subscription Manipulation:**
- Average cancellation: 8+ minutes vs 1-2 click signup
- Forced surveys, phone calls, typed confirmations
- "Confirmshaming" guilt tactics
- Hidden renewal terms

```python
class PricingManipulationType(Enum):
    DYNAMIC_PRICING = "real_time_price_adjustment"
    PERSONALIZED_PRICING = "surveillance_pricing"
    ANCHOR_PRICING = "reference_price_manipulation"
    DECOY_PRICING = "asymmetric_dominance"
    DRIP_PRICING = "hidden_fees_revealed_late"
    PARTITIONED_PRICING = "split_price_components"
    CHARM_PRICING = "psychological_pricing"
    ARTIFICIAL_SCARCITY = "fake_limited_stock"
    TIME_PRESSURE = "countdown_urgency"
    SUBSCRIPTION_TRAP = "difficult_cancellation"

@dataclass
class PricingAnalysis:
    """Analysis of pricing manipulation"""
    manipulation_types: List[PricingManipulationType] = field(default_factory=list)
    anchor_effect_strength: float = 0.0
    decoy_detected: bool = False
    drip_pricing_amount: float = 0.0
    true_price_vs_displayed: float = 0.0
    urgency_tactics: List[str] = field(default_factory=list)
    overall_manipulation_score: float = 0.0

class EconomicManipulationDetector:
    """
    Detects pricing and economic manipulation tactics.

    Research basis:
    - AIMultiple 2026: Dynamic pricing algorithms
    - ResearchGate 2024: Anchoring and decoy pricing
    - FTC 2024: Surveillance pricing investigation
    - CHI 2024: Subscription cancellation analysis
    """

    # Charm pricing patterns
    CHARM_PRICES = ['.99', '.95', '.97', '.49']

    # Urgency language patterns
    URGENCY_PATTERNS = [
        'only .* left', 'limited stock', 'selling fast',
        'ends in', 'expires', 'last chance', 'hurry',
        '.* people viewing', 'in .* carts', 'just sold'
    ]

    # Drip pricing signals
    DRIP_PRICING_SIGNALS = [
        'service fee', 'processing fee', 'convenience fee',
        'handling', 'delivery', 'taxes not included',
        'additional charges may apply', 'plus fees'
    ]

    def __init__(self):
        self.price_history = {}

    def analyze_pricing_page(self, page_data: Dict) -> PricingAnalysis:
        """
        Analyze a pricing page for manipulation tactics.

        Expected page_data:
        {
            'prices': [{'name': str, 'displayed_price': float, 'features': List[str]}],
            'original_prices': [float],  # Strikethrough prices
            'urgency_elements': List[str],
            'fine_print': str,
            'checkout_flow': [{'step': int, 'new_charges': float}]
        }
        """
        analysis = PricingAnalysis()

        prices = page_data.get('prices', [])
        original_prices = page_data.get('original_prices', [])

        # Analyze anchor pricing
        if original_prices and prices:
            for i, orig in enumerate(original_prices):
                if i < len(prices) and orig > 0:
                    discount_shown = (orig - prices[i]['displayed_price']) / orig
                    if discount_shown > 0.3:  # More than 30% "discount"
                        analysis.manipulation_types.append(PricingManipulationType.ANCHOR_PRICING)
                        analysis.anchor_effect_strength = discount_shown
                        break

        # Detect decoy pricing
        if len(prices) >= 3:
            decoy_result = self._detect_decoy(prices)
            if decoy_result['decoy_detected']:
                analysis.decoy_detected = True
                analysis.manipulation_types.append(PricingManipulationType.DECOY_PRICING)

        # Analyze drip pricing
        checkout_flow = page_data.get('checkout_flow', [])
        if checkout_flow:
            initial_price = checkout_flow[0].get('total', 0) if checkout_flow else 0
            final_price = checkout_flow[-1].get('total', 0) if checkout_flow else 0

            if final_price > initial_price * 1.1:  # More than 10% increase
                analysis.drip_pricing_amount = final_price - initial_price
                analysis.true_price_vs_displayed = final_price / initial_price if initial_price > 0 else 1
                analysis.manipulation_types.append(PricingManipulationType.DRIP_PRICING)

        # Check fine print for hidden fees
        fine_print = page_data.get('fine_print', '').lower()
        for signal in self.DRIP_PRICING_SIGNALS:
            if signal in fine_print:
                if PricingManipulationType.DRIP_PRICING not in analysis.manipulation_types:
                    analysis.manipulation_types.append(PricingManipulationType.DRIP_PRICING)
                break

        # Analyze urgency tactics
        urgency_elements = page_data.get('urgency_elements', [])
        for element in urgency_elements:
            element_lower = element.lower()
            for pattern in self.URGENCY_PATTERNS:
                if re.search(pattern, element_lower):
                    analysis.urgency_tactics.append(element)
                    break

        if analysis.urgency_tactics:
            analysis.manipulation_types.append(PricingManipulationType.TIME_PRESSURE)

            # Check for artificial scarcity
            if any('left' in t.lower() or 'stock' in t.lower() for t in analysis.urgency_tactics):
                analysis.manipulation_types.append(PricingManipulationType.ARTIFICIAL_SCARCITY)

        # Check for charm pricing
        for price in prices:
            price_str = str(price.get('displayed_price', 0))
            if any(charm in price_str for charm in self.CHARM_PRICES):
                analysis.manipulation_types.append(PricingManipulationType.CHARM_PRICING)
                break

        # Calculate overall manipulation score
        analysis.overall_manipulation_score = min(1.0,
            len(analysis.manipulation_types) * 0.15 +
            analysis.anchor_effect_strength * 0.2 +
            (0.3 if analysis.decoy_detected else 0) +
            min(0.3, analysis.drip_pricing_amount / 50) +
            len(analysis.urgency_tactics) * 0.1
        )

        return analysis

    def _detect_decoy(self, prices: List[Dict]) -> Dict:
        """
        Detect decoy pricing pattern (asymmetric dominance).

        A decoy is inferior to one option but not clearly inferior to another,
        making the target option look better by comparison.
        """
        result = {
            'decoy_detected': False,
            'decoy_index': None,
            'target_index': None,
            'competitor_index': None
        }

        if len(prices) < 3:
            return result

        # Simple heuristic: middle option is often the decoy
        # Check if middle option has poor value compared to higher option
        sorted_prices = sorted(prices, key=lambda x: x.get('displayed_price', 0))

        for i in range(1, len(sorted_prices) - 1):
            lower = sorted_prices[i - 1]
            middle = sorted_prices[i]
            higher = sorted_prices[i + 1]

            lower_price = lower.get('displayed_price', 0)
            middle_price = middle.get('displayed_price', 0)
            higher_price = higher.get('displayed_price', 0)

            # If middle is close to higher in price but has significantly fewer features
            if middle_price > lower_price * 1.3:  # Middle is >30% more than lower
                price_diff_to_higher = higher_price - middle_price
                price_diff_to_lower = middle_price - lower_price

                # If small price jump to higher but big jump from lower
                if price_diff_to_higher < price_diff_to_lower * 0.5:
                    result['decoy_detected'] = True
                    result['decoy_index'] = i
                    result['target_index'] = i + 1  # Higher option is target
                    result['competitor_index'] = i - 1
                    break

        return result

    def track_price_changes(self, product_id: str, current_price: float, timestamp: float) -> Dict:
        """
        Track price changes over time to detect dynamic pricing.
        """
        if product_id not in self.price_history:
            self.price_history[product_id] = []

        self.price_history[product_id].append({
            'price': current_price,
            'timestamp': timestamp
        })

        history = self.price_history[product_id]

        analysis = {
            'price_changes_detected': len(history) > 1,
            'change_frequency': 0,
            'price_volatility': 0.0,
            'dynamic_pricing_likely': False,
            'trend': 'stable'
        }

        if len(history) >= 2:
            prices = [h['price'] for h in history]
            timestamps = [h['timestamp'] for h in history]

            # Calculate change frequency
            time_span = timestamps[-1] - timestamps[0]
            if time_span > 0:
                changes = sum(1 for i in range(1, len(prices)) if prices[i] != prices[i-1])
                analysis['change_frequency'] = changes / (time_span / 3600)  # Changes per hour

            # Calculate volatility
            if len(prices) >= 3:
                analysis['price_volatility'] = np.std(prices) / np.mean(prices) if np.mean(prices) > 0 else 0

            # Detect dynamic pricing
            if analysis['change_frequency'] > 0.5 or analysis['price_volatility'] > 0.1:
                analysis['dynamic_pricing_likely'] = True

            # Determine trend
            if prices[-1] > prices[0] * 1.05:
                analysis['trend'] = 'increasing'
            elif prices[-1] < prices[0] * 0.95:
                analysis['trend'] = 'decreasing'

        return analysis


class SubscriptionTrapDetector:
    """
    Detects subscription manipulation patterns.

    Research basis:
    - CHI 2024: "Staying at the Roach Motel"
    - FTC 2024: Amazon Prime lawsuit
    - EU DSA 2024: Dark pattern regulations
    """

    # Cancellation friction patterns
    CANCELLATION_FRICTION_PATTERNS = {
        'phone_required': {
            'patterns': ['call to cancel', 'speak to representative', 'phone only'],
            'friction_score': 0.8
        },
        'multiple_steps': {
            'patterns': ['several steps', 'multiple pages', 'confirm again'],
            'friction_score': 0.5
        },
        'hidden_option': {
            'patterns': ['hard to find', 'buried', 'not obvious'],
            'friction_score': 0.6
        },
        'emotional_manipulation': {
            'patterns': ['we\'ll miss you', 'are you sure', 'you\'ll lose', 'sad to see'],
            'friction_score': 0.4
        },
        'forced_survey': {
            'patterns': ['tell us why', 'feedback required', 'survey before'],
            'friction_score': 0.3
        },
        'retention_gauntlet': {
            'patterns': ['special offer', 'discount to stay', 'pause instead'],
            'friction_score': 0.3
        }
    }

    def analyze_subscription_flow(self, flow_data: Dict) -> Dict:
        """
        Analyze subscription signup and cancellation flows.

        Expected flow_data:
        {
            'signup_steps': int,
            'signup_time_seconds': float,
            'cancel_steps': int,
            'cancel_time_seconds': float,
            'cancel_method': str,  # 'online', 'phone', 'email', 'mail'
            'cancel_page_text': str,
            'renewal_disclosure': str,  # Where/how renewal terms disclosed
            'trial_to_paid_friction': float  # 0-1
        }
        """
        analysis = {
            'roach_motel_detected': False,
            'friction_asymmetry_ratio': 0.0,
            'friction_types': [],
            'total_friction_score': 0.0,
            'regulatory_violations': [],
            'recommendations': []
        }

        signup_steps = flow_data.get('signup_steps', 1)
        cancel_steps = flow_data.get('cancel_steps', 1)
        signup_time = flow_data.get('signup_time_seconds', 60)
        cancel_time = flow_data.get('cancel_time_seconds', 60)

        # Calculate asymmetry
        step_ratio = cancel_steps / signup_steps if signup_steps > 0 else 1
        time_ratio = cancel_time / signup_time if signup_time > 0 else 1

        analysis['friction_asymmetry_ratio'] = max(step_ratio, time_ratio)

        if analysis['friction_asymmetry_ratio'] > 2:
            analysis['roach_motel_detected'] = True

        # Analyze cancellation method
        cancel_method = flow_data.get('cancel_method', 'online').lower()
        if cancel_method == 'phone':
            analysis['friction_types'].append('phone_required')
            analysis['total_friction_score'] += 0.8
            analysis['regulatory_violations'].append('EU DSA: Cancel must be as easy as signup')

        # Analyze cancel page text
        cancel_text = flow_data.get('cancel_page_text', '').lower()
        for friction_type, data in self.CANCELLATION_FRICTION_PATTERNS.items():
            for pattern in data['patterns']:
                if pattern in cancel_text:
                    analysis['friction_types'].append(friction_type)
                    analysis['total_friction_score'] += data['friction_score']
                    break

        # Check renewal disclosure
        renewal_disclosure = flow_data.get('renewal_disclosure', '')
        if not renewal_disclosure or 'fine print' in renewal_disclosure.lower():
            analysis['regulatory_violations'].append('FTC ROSCA: Clear renewal disclosure required')

        # Normalize friction score
        analysis['total_friction_score'] = min(1.0, analysis['total_friction_score'])

        # Generate recommendations
        if analysis['roach_motel_detected']:
            analysis['recommendations'].extend([
                'Cancellation should require same effort as signup',
                'Provide clear online cancellation option',
                'Remove unnecessary confirmation steps'
            ])

        if 'emotional_manipulation' in analysis['friction_types']:
            analysis['recommendations'].append('Remove guilt-inducing language from cancellation flow')

        return analysis
```

---

## 8. AI-SPECIFIC MANIPULATION

### Research Findings

**LLM Persuasion (2024-2025):**
- LLMs can exceed human persuasion in controlled settings
- GPT-4 with personal info: 81.7% higher agreement odds
- Post-training methods boosted persuasiveness 51%
- Increased persuasion often correlated with DECREASED factual accuracy
- Scaling model size shows diminishing returns for persuasion

**Deepfakes (2024):**
- $12 billion in deepfake-enabled fraud (projected $40B in 3 years)
- 1 in 4 adults experienced AI voice scams
- Best detectors only 75% accurate
- "Impostor Bias" - people question even authentic media
- January 2024: AI Biden robocall attempted election manipulation

**AI-Generated Content:**
- 68% concerned about AI manipulation
- Detection tools 50% less effective on "in the wild" deepfakes
- Adversarial perturbations reduce detection 40%

```python
class AIManipulationType(Enum):
    LLM_PERSUASION = "llm_generated_persuasion"
    DEEPFAKE_VIDEO = "synthetic_video"
    DEEPFAKE_AUDIO = "voice_cloning"
    DEEPFAKE_IMAGE = "synthetic_image"
    AI_PERSONALIZATION = "algorithmic_targeting"
    CHATBOT_MANIPULATION = "conversational_ai_exploitation"
    SYNTHETIC_SOCIAL_PROOF = "ai_generated_reviews"
    AUTOMATED_DISINFORMATION = "ai_disinformation_campaign"

@dataclass
class AIContentAnalysis:
    """Analysis of AI-generated content"""
    ai_generated_probability: float = 0.0
    manipulation_type: Optional[AIManipulationType] = None
    authenticity_indicators: List[str] = field(default_factory=list)
    synthetic_markers: List[str] = field(default_factory=list)
    risk_level: str = "unknown"
    confidence: float = 0.0

class AIManipulationDetector:
    """
    Detects AI-generated manipulation content.

    Research basis:
    - Science 2025: Levers of political persuasion with AI
    - arXiv 2025: LLM as dangerous persuader
    - Nature 2025: Meta-analysis of LLM persuasive power
    - PMC 2025: Deepfake detection survey
    - Deloitte 2025: Deepfake disruption report
    """

    # LLM-generated text indicators
    LLM_TEXT_INDICATORS = {
        'excessive_hedging': [
            'it\'s important to note', 'it should be mentioned',
            'one might argue', 'it could be said'
        ],
        'formal_transitions': [
            'furthermore', 'moreover', 'additionally', 'consequently',
            'nevertheless', 'notwithstanding'
        ],
        'ai_phrases': [
            'as an ai', 'i don\'t have personal', 'i cannot',
            'it\'s worth noting', 'in conclusion'
        ],
        'balanced_framing': [
            'on the other hand', 'however', 'while some argue',
            'both sides', 'perspectives vary'
        ]
    }

    # Deepfake detection heuristics
    DEEPFAKE_VIDEO_INDICATORS = {
        'facial_inconsistencies': [
            'eye_blink_irregular', 'lip_sync_mismatch', 'face_boundary_artifacts',
            'lighting_inconsistency', 'head_pose_unnatural'
        ],
        'temporal_artifacts': [
            'frame_flickering', 'temporal_coherence_loss', 'motion_blur_missing'
        ],
        'quality_indicators': [
            'resolution_mismatch', 'compression_artifacts', 'color_inconsistency'
        ]
    }

    # Persuasion technique indicators from research
    PERSUASION_TECHNIQUES = {
        'personalization': {
            'indicators': ['based on your', 'tailored for you', 'your interests'],
            'effectiveness_boost': 0.82  # 81.7% from research
        },
        'emotional_appeal': {
            'indicators': ['feel', 'imagine', 'picture yourself', 'experience'],
            'effectiveness_boost': 0.51  # 51% from post-training methods
        },
        'social_proof_synthetic': {
            'indicators': ['thousands have', 'everyone is', 'popular choice'],
            'effectiveness_boost': 0.30
        },
        'authority_citation': {
            'indicators': ['experts say', 'studies show', 'research indicates'],
            'effectiveness_boost': 0.27  # 27% from prompting methods
        }
    }

    def analyze_text_for_ai_generation(self, text: str) -> AIContentAnalysis:
        """
        Analyze text for AI generation indicators.
        """
        analysis = AIContentAnalysis()
        text_lower = text.lower()

        indicator_counts = {category: 0 for category in self.LLM_TEXT_INDICATORS}

        for category, phrases in self.LLM_TEXT_INDICATORS.items():
            for phrase in phrases:
                if phrase in text_lower:
                    indicator_counts[category] += 1
                    analysis.synthetic_markers.append(f"{category}: {phrase}")

        # Calculate AI probability based on indicators
        total_indicators = sum(indicator_counts.values())
        text_length = len(text.split())

        # Normalize by text length (longer texts naturally have more phrases)
        indicator_density = total_indicators / (text_length / 100) if text_length > 0 else 0

        # AI text tends to have multiple categories present
        categories_present = sum(1 for c in indicator_counts.values() if c > 0)

        analysis.ai_generated_probability = min(1.0,
            indicator_density * 0.3 +
            categories_present * 0.15
        )

        # Check for persuasion techniques
        persuasion_detected = []
        for technique, data in self.PERSUASION_TECHNIQUES.items():
            if any(ind in text_lower for ind in data['indicators']):
                persuasion_detected.append(technique)

        if persuasion_detected:
            analysis.manipulation_type = AIManipulationType.LLM_PERSUASION
            analysis.ai_generated_probability += 0.1 * len(persuasion_detected)

        # Determine risk level
        if analysis.ai_generated_probability > 0.7:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.4:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        analysis.confidence = min(1.0, 0.3 + total_indicators * 0.1)

        return analysis

    def analyze_conversation_for_chatbot_manipulation(
        self,
        messages: List[Dict],
        claimed_identity: str = ""
    ) -> Dict:
        """
        Analyze conversation for AI chatbot manipulation patterns.

        Research shows chatbots can use therapeutic rapport techniques
        for manipulation purposes.
        """
        analysis = {
            'chatbot_suspected': False,
            'manipulation_patterns': [],
            'rapport_building_detected': False,
            'personalization_level': 0.0,
            'risk_score': 0.0
        }

        if not messages:
            return analysis

        # Analyze response patterns
        response_lengths = []
        response_times = []
        formality_scores = []

        for i, msg in enumerate(messages):
            if msg.get('role') == 'assistant' or msg.get('sender') == claimed_identity:
                content = msg.get('content', '')
                response_lengths.append(len(content.split()))

                # Check for AI-like consistency
                if i > 0:
                    prev_time = messages[i-1].get('timestamp', 0)
                    curr_time = msg.get('timestamp', 0)
                    if curr_time > prev_time:
                        response_times.append(curr_time - prev_time)

        # AI chatbots often have consistent response lengths
        if response_lengths:
            length_cv = np.std(response_lengths) / np.mean(response_lengths) if np.mean(response_lengths) > 0 else 1
            if length_cv < 0.3:  # Very consistent
                analysis['chatbot_suspected'] = True
                analysis['manipulation_patterns'].append('CONSISTENT_RESPONSE_LENGTH')

        # AI chatbots often respond quickly and consistently
        if response_times:
            time_cv = np.std(response_times) / np.mean(response_times) if np.mean(response_times) > 0 else 1
            if time_cv < 0.2:  # Very consistent timing
                analysis['manipulation_patterns'].append('CONSISTENT_RESPONSE_TIME')

        # Check for rapport-building techniques
        rapport_phrases = [
            'i understand', 'that must be', 'i hear you',
            'tell me more', 'how does that make you feel'
        ]

        rapport_count = 0
        for msg in messages:
            content = msg.get('content', '').lower()
            if any(phrase in content for phrase in rapport_phrases):
                rapport_count += 1

        if rapport_count > len(messages) * 0.2:
            analysis['rapport_building_detected'] = True
            analysis['manipulation_patterns'].append('THERAPEUTIC_RAPPORT_TECHNIQUES')

        # Check for personalization (using user's info against them)
        user_messages = [m for m in messages if m.get('role') == 'user' or m.get('sender') != claimed_identity]
        assistant_messages = [m for m in messages if m.get('role') == 'assistant' or m.get('sender') == claimed_identity]

        # Look for echoed personal details
        user_text = ' '.join(m.get('content', '') for m in user_messages).lower()
        for msg in assistant_messages:
            content = msg.get('content', '').lower()

            # Simple check: does assistant reference specific user details?
            personal_echoes = sum(1 for word in user_text.split()
                                 if len(word) > 5 and word in content)

            if personal_echoes > 3:
                analysis['personalization_level'] = min(1.0, personal_echoes / 10)
                analysis['manipulation_patterns'].append('PERSONAL_INFO_EXPLOITATION')

        # Calculate risk score
        analysis['risk_score'] = min(1.0,
            (0.3 if analysis['chatbot_suspected'] else 0) +
            (0.2 if analysis['rapport_building_detected'] else 0) +
            analysis['personalization_level'] * 0.3 +
            len(analysis['manipulation_patterns']) * 0.1
        )

        return analysis


class DeepfakeDetector:
    """
    Detects deepfake and synthetic media.

    Research basis:
    - PMC 2025: Deepfake forensics survey
    - GAO 2024: Combating deepfakes spotlight
    - Springer 2025: Multimedia deepfake detection
    """

    # Based on research: best detectors only 75% accurate
    DETECTION_CONFIDENCE_CAP = 0.75

    def analyze_video_authenticity(self, video_features: Dict) -> AIContentAnalysis:
        """
        Analyze video for deepfake indicators.

        Expected video_features:
        {
            'face_detection_consistency': float,  # 0-1
            'blink_pattern_score': float,  # 0-1, 1 = natural
            'lip_sync_score': float,  # 0-1, 1 = perfect sync
            'lighting_consistency': float,  # 0-1
            'temporal_coherence': float,  # 0-1
            'compression_artifacts': float,  # 0-1, higher = more artifacts
            'face_boundary_quality': float,  # 0-1
            'source_metadata': Dict
        }
        """
        analysis = AIContentAnalysis()
        analysis.manipulation_type = AIManipulationType.DEEPFAKE_VIDEO

        scores = []
        weights = []

        # Blink pattern (deepfakes often have irregular blinking)
        blink_score = video_features.get('blink_pattern_score', 0.5)
        if blink_score < 0.5:
            analysis.synthetic_markers.append('IRREGULAR_BLINK_PATTERN')
        scores.append(1 - blink_score)
        weights.append(0.2)

        # Lip sync (AI struggles with perfect lip sync)
        lip_sync = video_features.get('lip_sync_score', 0.5)
        if lip_sync < 0.7:
            analysis.synthetic_markers.append('LIP_SYNC_MISMATCH')
        scores.append(1 - lip_sync)
        weights.append(0.25)

        # Lighting consistency
        lighting = video_features.get('lighting_consistency', 0.5)
        if lighting < 0.6:
            analysis.synthetic_markers.append('LIGHTING_INCONSISTENCY')
        scores.append(1 - lighting)
        weights.append(0.15)

        # Temporal coherence (frame-to-frame consistency)
        temporal = video_features.get('temporal_coherence', 0.5)
        if temporal < 0.6:
            analysis.synthetic_markers.append('TEMPORAL_ARTIFACTS')
        scores.append(1 - temporal)
        weights.append(0.2)

        # Face boundary quality
        boundary = video_features.get('face_boundary_quality', 0.5)
        if boundary < 0.7:
            analysis.synthetic_markers.append('FACE_BOUNDARY_ARTIFACTS')
        scores.append(1 - boundary)
        weights.append(0.2)

        # Calculate weighted probability
        weighted_sum = sum(s * w for s, w in zip(scores, weights))
        total_weight = sum(weights)

        analysis.ai_generated_probability = min(
            self.DETECTION_CONFIDENCE_CAP,
            weighted_sum / total_weight if total_weight > 0 else 0
        )

        # Check metadata
        metadata = video_features.get('source_metadata', {})
        if metadata.get('editing_software') in ['Runway', 'Synthesia', 'DeepFaceLab']:
            analysis.synthetic_markers.append('KNOWN_DEEPFAKE_SOFTWARE_METADATA')
            analysis.ai_generated_probability = min(0.9, analysis.ai_generated_probability + 0.3)

        # Determine risk level
        if analysis.ai_generated_probability > 0.6:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.35:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        # Confidence based on marker count
        analysis.confidence = min(self.DETECTION_CONFIDENCE_CAP,
            0.3 + len(analysis.synthetic_markers) * 0.1)

        # Add authenticity indicators
        if analysis.ai_generated_probability < 0.3:
            analysis.authenticity_indicators = [
                'NATURAL_BLINK_PATTERN',
                'CONSISTENT_LIGHTING',
                'SMOOTH_TEMPORAL_FLOW'
            ]

        return analysis

    def analyze_audio_authenticity(self, audio_features: Dict) -> AIContentAnalysis:
        """
        Analyze audio for voice cloning/deepfake indicators.

        Expected audio_features:
        {
            'spectral_consistency': float,
            'breathing_patterns': float,  # 0-1, 1 = natural
            'micro_pauses': float,  # Natural speech has micro-pauses
            'pitch_variation': float,
            'background_consistency': float,
            'clipping_artifacts': float
        }
        """
        analysis = AIContentAnalysis()
        analysis.manipulation_type = AIManipulationType.DEEPFAKE_AUDIO

        # Breathing patterns (cloned voices often lack natural breathing)
        breathing = audio_features.get('breathing_patterns', 0.5)
        if breathing < 0.4:
            analysis.synthetic_markers.append('MISSING_BREATH_SOUNDS')

        # Micro-pauses (AI often too fluent)
        pauses = audio_features.get('micro_pauses', 0.5)
        if pauses < 0.3:
            analysis.synthetic_markers.append('UNNATURAL_FLUENCY')

        # Pitch variation (cloned voices may have limited variation)
        pitch_var = audio_features.get('pitch_variation', 0.5)
        if pitch_var < 0.4:
            analysis.synthetic_markers.append('LIMITED_PITCH_VARIATION')

        # Background consistency (AI may have too-clean background)
        background = audio_features.get('background_consistency', 0.5)
        if background > 0.95:  # Too consistent = suspicious
            analysis.synthetic_markers.append('UNNATURALLY_CLEAN_BACKGROUND')

        # Calculate probability
        marker_count = len(analysis.synthetic_markers)
        analysis.ai_generated_probability = min(
            self.DETECTION_CONFIDENCE_CAP,
            marker_count * 0.2
        )

        if analysis.ai_generated_probability > 0.5:
            analysis.risk_level = "high"
        elif analysis.ai_generated_probability > 0.25:
            analysis.risk_level = "medium"
        else:
            analysis.risk_level = "low"

        analysis.confidence = min(0.7, 0.3 + marker_count * 0.1)

        return analysis
```

---

## 9. INTERVENTION EFFECTIVENESS ANALYSIS

### Research Findings

**Media Literacy Interventions (2024):**
- Meta-analysis (N=81,155): Overall effect d=0.60
- Reduces belief in misinformation (d=0.27)
- Improves discernment (d=0.76)
- Decreases sharing (d=1.04)
- Multiple sessions (d=1.93) >> single session (d=0.26)

**Friction Interventions:**
- Short delays before app opening increase intentional use
- Warning labels reduce sharing but not belief
- Cooling-off periods effective for purchases

**Inoculation Theory:**
- "Prebunking" reduces misinformation endorsement (d=-0.36)
- Teaching manipulation tactics more effective than fact-checking
- Effects decay without reinforcement

```python
class InterventionType(Enum):
    MEDIA_LITERACY = "media_literacy_education"
    FRICTION = "behavioral_friction"
    INOCULATION = "prebunking_inoculation"
    WARNING_LABEL = "content_warning"
    COOLING_OFF = "decision_delay"
    TRANSPARENCY = "disclosure_requirement"
    DESIGN_CHANGE = "ethical_design_modification"

@dataclass
class InterventionEffectiveness:
    """Measured effectiveness of an intervention"""
    intervention_type: InterventionType
    effect_size: float  # Cohen's d or similar
    confidence_interval: Tuple[float, float]
    duration_of_effect: str  # "immediate", "short-term", "long-term"
    decay_rate: float  # How quickly effect diminishes
    population_moderators: List[str]
    implementation_cost: str  # "low", "medium", "high"
    scalability: str  # "low", "medium", "high"

class InterventionAnalyzer:
    """
    Analyzes and recommends interventions against manipulation.

    Research basis:
    - Sage 2024: Media literacy meta-analysis
    - arXiv 2024: Design frictions on social media
    - Various inoculation theory research
    """

    # Evidence-based intervention effectiveness from research
    INTERVENTION_EVIDENCE = {
        InterventionType.MEDIA_LITERACY: {
            'overall_effect': 0.60,
            'belief_reduction': 0.27,
            'discernment_improvement': 0.76,
            'sharing_reduction': 1.04,
            'multiple_sessions_effect': 1.93,
            'single_session_effect': 0.26,
            'decay_rate': 0.3,  # Effect decays ~30% without reinforcement
            'moderators': ['education_level', 'age', 'prior_exposure']
        },
        InterventionType.INOCULATION: {
            'overall_effect': 0.36,
            'misinformation_endorsement_reduction': 0.36,
            'manipulation_recognition_improvement': 0.45,
            'decay_rate': 0.25,
            'boosters_recommended': True
        },
        InterventionType.FRICTION: {
            'intentional_use_increase': 0.30,
            'mindless_scrolling_reduction': 0.40,
            'optimal_delay_seconds': 3,
            'effectiveness_at_home': 'reduced',  # Per research
            'effectiveness_other_settings': 'higher'
        },
        InterventionType.WARNING_LABEL: {
            'sharing_reduction': 0.20,
            'belief_reduction': 0.10,  # Less effective for beliefs
            'reactance_risk': 0.15  # Can backfire
        },
        InterventionType.COOLING_OFF: {
            'impulse_purchase_reduction': 0.35,
            'regret_reduction': 0.40,
            'optimal_period_hours': 24
        }
    }

    def recommend_interventions(
        self,
        manipulation_analysis: Dict,
        target_population: Dict = None
    ) -> List[Dict]:
        """
        Recommend interventions based on detected manipulation.

        Args:
            manipulation_analysis: Results from various detectors
            target_population: Demographics and characteristics
        """
        recommendations = []

        # Analyze what manipulations were detected
        manipulation_types = manipulation_analysis.get('manipulation_types', [])
        risk_score = manipulation_analysis.get('overall_risk_score', 0)

        # High-risk situations need multiple interventions
        if risk_score > 0.7:
            recommendations.append({
                'intervention': InterventionType.FRICTION,
                'priority': 'high',
                'rationale': 'Immediate friction to slow decision-making',
                'implementation': 'Add 3-5 second delay before action',
                'expected_effect': 0.40
            })

        # Media literacy for ongoing protection
        if any(m in str(manipulation_types) for m in ['misinformation', 'fake', 'deepfake']):
            recommendations.append({
                'intervention': InterventionType.MEDIA_LITERACY,
                'priority': 'high',
                'rationale': 'Build long-term resistance to misinformation',
                'implementation': 'Multi-session program (4+ sessions)',
                'expected_effect': 1.93,
                'note': 'Single sessions only achieve d=0.26'
            })

        # Inoculation for predictable manipulation patterns
        if any(m in str(manipulation_types) for m in ['scarcity', 'urgency', 'authority']):
            recommendations.append({
                'intervention': InterventionType.INOCULATION,
                'priority': 'medium',
                'rationale': 'Prebunk common manipulation tactics',
                'implementation': 'Explain tactic mechanisms before exposure',
                'expected_effect': 0.36
            })

        # Warning labels for specific content
        if 'emotional_manipulation' in str(manipulation_types):
            recommendations.append({
                'intervention': InterventionType.WARNING_LABEL,
                'priority': 'medium',
                'rationale': 'Alert to emotional manipulation',
                'implementation': 'Contextual warning before content',
                'expected_effect': 0.20,
                'caution': 'May not reduce belief, mainly reduces sharing'
            })

        # Cooling-off for financial manipulation
        if any(m in str(manipulation_types) for m in ['pricing', 'subscription', 'purchase']):
            recommendations.append({
                'intervention': InterventionType.COOLING_OFF,
                'priority': 'high',
                'rationale': 'Prevent impulse decisions',
                'implementation': '24-hour delay for significant purchases',
                'expected_effect': 0.35
            })

        # Adjust for population factors
        if target_population:
            recommendations = self._adjust_for_population(recommendations, target_population)

        return sorted(recommendations, key=lambda x: x.get('priority', 'low') == 'high', reverse=True)

    def _adjust_for_population(self, recommendations: List[Dict], population: Dict) -> List[Dict]:
        """Adjust recommendations based on target population"""
        age = population.get('age', 30)

        for rec in recommendations:
            # Media literacy more effective for college students
            if rec['intervention'] == InterventionType.MEDIA_LITERACY:
                if 18 <= age <= 25:
                    rec['expected_effect'] *= 1.2
                    rec['note'] = rec.get('note', '') + ' Higher effect for college-age.'

            # Friction less effective at home (per research)
            if rec['intervention'] == InterventionType.FRICTION:
                if population.get('context') == 'home':
                    rec['expected_effect'] *= 0.7
                    rec['caution'] = 'Reduced effectiveness in home settings'

        return recommendations

    def calculate_combined_intervention_effect(
        self,
        interventions: List[InterventionType]
    ) -> Dict:
        """
        Calculate expected combined effect of multiple interventions.

        Note: Effects don't simply add; there are diminishing returns.
        """
        if not interventions:
            return {'combined_effect': 0, 'synergies': [], 'conflicts': []}

        effects = []
        for intervention in interventions:
            if intervention in self.INTERVENTION_EVIDENCE:
                effects.append(self.INTERVENTION_EVIDENCE[intervention].get('overall_effect', 0))

        # Apply diminishing returns formula
        # Each additional intervention adds less
        combined = 0
        for i, effect in enumerate(sorted(effects, reverse=True)):
            # Each subsequent intervention has reduced marginal effect
            diminishing_factor = 1 / (1 + i * 0.3)
            combined += effect * diminishing_factor

        result = {
            'combined_effect': min(2.0, combined),  # Cap at very large effect
            'synergies': [],
            'conflicts': []
        }

        # Check for synergies
        if InterventionType.INOCULATION in interventions and InterventionType.MEDIA_LITERACY in interventions:
            result['synergies'].append('Inoculation + Media Literacy: Complementary approaches')
            result['combined_effect'] *= 1.1

        # Check for conflicts
        if InterventionType.WARNING_LABEL in interventions and len(interventions) > 2:
            result['conflicts'].append('Too many interventions may cause warning fatigue')
            result['combined_effect'] *= 0.9

        return result


class InterventionDecayTracker:
    """
    Tracks intervention effectiveness over time.

    Research shows effects decay without reinforcement.
    """

    def __init__(self):
        self.intervention_history = {}

    def record_intervention(
        self,
        user_id: str,
        intervention: InterventionType,
        timestamp: float,
        initial_effect: float
    ):
        """Record when an intervention was applied"""
        if user_id not in self.intervention_history:
            self.intervention_history[user_id] = []

        self.intervention_history[user_id].append({
            'intervention': intervention,
            'timestamp': timestamp,
            'initial_effect': initial_effect
        })

    def calculate_current_protection_level(
        self,
        user_id: str,
        current_time: float
    ) -> Dict:
        """Calculate current protection level accounting for decay"""
        if user_id not in self.intervention_history:
            return {'protection_level': 0, 'recommendations': ['No interventions recorded']}

        history = self.intervention_history[user_id]

        total_protection = 0
        decayed_interventions = []

        for record in history:
            intervention = record['intervention']
            elapsed_days = (current_time - record['timestamp']) / 86400

            # Get decay rate from evidence base
            decay_rate = InterventionAnalyzer.INTERVENTION_EVIDENCE.get(
                intervention, {}
            ).get('decay_rate', 0.3)

            # Exponential decay model
            remaining_effect = record['initial_effect'] * np.exp(-decay_rate * elapsed_days / 30)

            total_protection += remaining_effect

            if remaining_effect < record['initial_effect'] * 0.5:
                decayed_interventions.append(intervention.value)

        result = {
            'protection_level': min(1.0, total_protection),
            'decayed_interventions': decayed_interventions,
            'recommendations': []
        }

        if decayed_interventions:
            result['recommendations'].append(
                f"Consider booster for: {', '.join(decayed_interventions)}"
            )

        if result['protection_level'] < 0.3:
            result['recommendations'].append("Protection level low - intervention recommended")

        return result
```

---

## 10. REGULATORY COMPLIANCE MAPPING

### Research Findings

**FTC Enforcement (2024-2025):**
- Amazon: $2.5 billion settlement for dark patterns
- Adobe: DOJ complaint for cancellation difficulty
- 76% of sites use dark patterns (international review)
- Click-to-Cancel rule adopted then vacated

**EU Regulations:**
- Digital Services Act (Feb 2024): Prohibits "making cancellation significantly more cumbersome than signup"
- AI Act: Classifies emotional manipulation as high-risk/prohibited
- German Fair Consumer Contracts Act: Requires termination button

**US State Laws:**
- CCPA: Explicit dark pattern prohibition
- 14 states with privacy/deceptive design laws

```python
class Jurisdiction(Enum):
    US_FEDERAL = "us_federal"
    US_CALIFORNIA = "us_california"
    EU = "european_union"
    UK = "united_kingdom"
    GERMANY = "germany"
    CANADA = "canada"
    AUSTRALIA = "australia"

class RegulationType(Enum):
    DARK_PATTERN_PROHIBITION = "dark_pattern"
    DECEPTIVE_ADVERTISING = "deceptive_advertising"
    SUBSCRIPTION_PRACTICES = "subscription_regulation"
    CHILD_PROTECTION = "children_online_protection"
    AI_REGULATION = "ai_specific"
    PRIVACY_DESIGN = "privacy_by_design"

@dataclass
class RegulatoryViolation:
    """Identified regulatory violation"""
    jurisdiction: Jurisdiction
    regulation_type: RegulationType
    specific_law: str
    violation_description: str
    severity: str  # "minor", "moderate", "severe"
    enforcement_likelihood: float
    potential_penalty: str
    remediation_steps: List[str]

class RegulatoryComplianceAnalyzer:
    """
    Maps detected manipulation to regulatory violations.

    Research basis:
    - FTC enforcement actions 2024
    - EU DSA requirements
    - State privacy law requirements
    """

    # Regulatory mappings
    REGULATION_DATABASE = {
        Jurisdiction.US_FEDERAL: {
            'ftc_section_5': {
                'name': 'FTC Act Section 5',
                'prohibits': ['deceptive_practices', 'unfair_practices'],
                'enforcement': 'Active - multiple 2024 cases',
                'penalties': 'Civil penalties, injunctions, refunds'
            },
            'rosca': {
                'name': 'Restore Online Shoppers Confidence Act',
                'prohibits': ['negative_option_without_consent', 'hidden_terms'],
                'enforcement': 'Active - Amazon case 2024',
                'penalties': 'Civil penalties up to $50,000+ per violation'
            }
        },
        Jurisdiction.US_CALIFORNIA: {
            'ccpa_cpra': {
                'name': 'California Consumer Privacy Act / CPRA',
                'prohibits': ['dark_patterns_in_consent', 'deceptive_design'],
                'enforcement': 'Active',
                'penalties': '$2,500-$7,500 per violation'
            }
        },
        Jurisdiction.EU: {
            'dsa': {
                'name': 'Digital Services Act',
                'prohibits': [
                    'cancellation_harder_than_signup',
                    'dark_patterns',
                    'manipulative_design'
                ],
                'enforcement': 'Active since Feb 2024',
                'penalties': 'Up to 6% global turnover'
            },
            'ai_act': {
                'name': 'EU AI Act',
                'prohibits': [
                    'subliminal_manipulation',
                    'exploitation_of_vulnerabilities',
                    'social_scoring'
                ],
                'enforcement': 'Phased implementation',
                'penalties': 'Up to 7% global turnover for prohibited practices'
            },
            'gdpr': {
                'name': 'General Data Protection Regulation',
                'prohibits': ['deceptive_consent', 'dark_patterns_in_privacy'],
                'enforcement': 'Active',
                'penalties': 'Up to 4% global turnover or EUR 20 million'
            }
        },
        Jurisdiction.GERMANY: {
            'fair_contracts_act': {
                'name': 'Fair Consumer Contracts Act',
                'prohibits': ['no_termination_button'],
                'enforcement': 'Active',
                'penalties': 'Varies'
            }
        }
    }

    # Mapping from manipulation types to regulations
    MANIPULATION_TO_REGULATION = {
        'roach_motel': [
            (Jurisdiction.EU, 'dsa'),
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.GERMANY, 'fair_contracts_act')
        ],
        'confirmshaming': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.EU, 'dsa')
        ],
        'fake_urgency': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.EU, 'dsa')
        ],
        'hidden_costs': [
            (Jurisdiction.US_FEDERAL, 'rosca'),
            (Jurisdiction.US_CALIFORNIA, 'ccpa_cpra')
        ],
        'dark_pattern_consent': [
            (Jurisdiction.EU, 'gdpr'),
            (Jurisdiction.US_CALIFORNIA, 'ccpa_cpra')
        ],
        'subliminal_manipulation': [
            (Jurisdiction.EU, 'ai_act')
        ],
        'child_targeted_manipulation': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),  # COPPA via FTC
            (Jurisdiction.EU, 'dsa')
        ],
        'deepfake_fraud': [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5')
            # Multiple state laws also apply
        ]
    }

    def analyze_compliance(
        self,
        manipulation_analysis: Dict,
        operating_jurisdictions: List[Jurisdiction] = None
    ) -> List[RegulatoryViolation]:
        """
        Analyze detected manipulation for regulatory compliance.
        """
        violations = []

        if operating_jurisdictions is None:
            operating_jurisdictions = list(Jurisdiction)

        manipulation_types = manipulation_analysis.get('manipulation_types', [])

        for manip_type in manipulation_types:
            manip_key = str(manip_type).lower().replace(' ', '_')

            # Find matching regulations
            for key, regulations in self.MANIPULATION_TO_REGULATION.items():
                if key in manip_key or manip_key in key:
                    for jurisdiction, reg_id in regulations:
                        if jurisdiction in operating_jurisdictions:
                            reg_info = self.REGULATION_DATABASE.get(jurisdiction, {}).get(reg_id, {})

                            if reg_info:
                                violation = RegulatoryViolation(
                                    jurisdiction=jurisdiction,
                                    regulation_type=self._get_regulation_type(reg_id),
                                    specific_law=reg_info.get('name', reg_id),
                                    violation_description=f"Detected {manip_type} may violate {reg_info.get('name')}",
                                    severity=self._assess_severity(manipulation_analysis, manip_type),
                                    enforcement_likelihood=self._assess_enforcement_likelihood(jurisdiction, reg_id),
                                    potential_penalty=reg_info.get('penalties', 'Unknown'),
                                    remediation_steps=self._generate_remediation(manip_type, reg_id)
                                )
                                violations.append(violation)

        return violations

    def _get_regulation_type(self, reg_id: str) -> RegulationType:
        """Map regulation ID to type"""
        mapping = {
            'ftc_section_5': RegulationType.DECEPTIVE_ADVERTISING,
            'rosca': RegulationType.SUBSCRIPTION_PRACTICES,
            'ccpa_cpra': RegulationType.PRIVACY_DESIGN,
            'dsa': RegulationType.DARK_PATTERN_PROHIBITION,
            'ai_act': RegulationType.AI_REGULATION,
            'gdpr': RegulationType.PRIVACY_DESIGN,
            'fair_contracts_act': RegulationType.SUBSCRIPTION_PRACTICES
        }
        return mapping.get(reg_id, RegulationType.DARK_PATTERN_PROHIBITION)

    def _assess_severity(self, analysis: Dict, manip_type: str) -> str:
        """Assess severity based on manipulation analysis"""
        risk_score = analysis.get('overall_risk_score', 0)

        if 'child' in str(manip_type).lower():
            return 'severe'  # Child-related always severe
        elif risk_score > 0.7:
            return 'severe'
        elif risk_score > 0.4:
            return 'moderate'
        else:
            return 'minor'

    def _assess_enforcement_likelihood(self, jurisdiction: Jurisdiction, reg_id: str) -> float:
        """Assess likelihood of enforcement"""
        # Based on 2024 enforcement activity
        high_enforcement = [
            (Jurisdiction.US_FEDERAL, 'ftc_section_5'),
            (Jurisdiction.US_FEDERAL, 'rosca'),
            (Jurisdiction.EU, 'dsa'),
            (Jurisdiction.EU, 'gdpr')
        ]

        if (jurisdiction, reg_id) in high_enforcement:
            return 0.7
        return 0.4

    def _generate_remediation(self, manip_type: str, reg_id: str) -> List[str]:
        """Generate remediation steps"""
        remediation = {
            'roach_motel': [
                'Make cancellation process equal in steps to signup',
                'Provide clear online cancellation option',
                'Add termination button (required in Germany)',
                'Remove unnecessary friction from cancellation'
            ],
            'fake_urgency': [
                'Remove countdown timers that reset',
                'Ensure scarcity claims are accurate and verifiable',
                'Add disclosure for limited-time offers'
            ],
            'confirmshaming': [
                'Use neutral language for decline options',
                'Remove guilt-inducing decline buttons',
                'Provide equal visual weight to all options'
            ],
            'hidden_costs': [
                'Display full price including all fees upfront',
                'Itemize additional charges clearly',
                'Obtain affirmative consent for each charge'
            ],
            'dark_pattern_consent': [
                'Implement clear, specific consent requests',
                'Avoid pre-checked boxes',
                'Make rejection as easy as acceptance'
            ]
        }

        for key, steps in remediation.items():
            if key in str(manip_type).lower():
                return steps

        return ['Review and modify design to comply with regulations']

    def generate_compliance_report(
        self,
        violations: List[RegulatoryViolation]
    ) -> Dict:
        """Generate comprehensive compliance report"""
        report = {
            'total_violations': len(violations),
            'by_jurisdiction': {},
            'by_severity': {'severe': 0, 'moderate': 0, 'minor': 0},
            'high_priority_remediations': [],
            'estimated_risk_exposure': 'Low'
        }

        for violation in violations:
            # Count by jurisdiction
            jur = violation.jurisdiction.value
            if jur not in report['by_jurisdiction']:
                report['by_jurisdiction'][jur] = 0
            report['by_jurisdiction'][jur] += 1

            # Count by severity
            report['by_severity'][violation.severity] += 1

            # Collect high-priority remediations
            if violation.severity == 'severe':
                report['high_priority_remediations'].extend(violation.remediation_steps)

        # Assess overall risk
        if report['by_severity']['severe'] > 0:
            report['estimated_risk_exposure'] = 'High'
        elif report['by_severity']['moderate'] > 2:
            report['estimated_risk_exposure'] = 'Medium'

        # Deduplicate remediations
        report['high_priority_remediations'] = list(set(report['high_priority_remediations']))

        return report
```

---

## MASTER INTEGRATION CLASS

```python
class ComprehensivePersuasionAuditor:
    """
    Master class integrating all detection frameworks.

    Provides unified interface for complete persuasion/manipulation auditing.
    """

    def __init__(self):
        # Initialize all detectors
        self.multimodal_detector = MultimodalPersuasionDetector()
        self.cut_rhythm_analyzer = CutRhythmAnalyzer()
        self.social_network_detector = SocialNetworkManipulationDetector()
        self.emotional_contagion_detector = EmotionalContagionDetector()
        self.echo_chamber_detector = EchoChAmberDetector()
        self.trust_detector = TrustExploitationDetector()
        self.grooming_detector = GroomingPatternDetector()
        self.platform_detector = PlatformManipulationDetector()
        self.infinite_scroll_detector = InfiniteScrollDetector()
        self.physiological_detector = PhysiologicalManipulationDetector()
        self.gaze_analyzer = GazePatternAnalyzer()
        self.vulnerability_detector = VulnerablePopulationDetector()
        self.child_safety_detector = ChildSafetyDetector()
        self.economic_detector = EconomicManipulationDetector()
        self.subscription_detector = SubscriptionTrapDetector()
        self.ai_detector = AIManipulationDetector()
        self.deepfake_detector = DeepfakeDetector()
        self.intervention_analyzer = InterventionAnalyzer()
        self.compliance_analyzer = RegulatoryComplianceAnalyzer()

    def full_audit(self, content_data: Dict, user_profile: Dict = None) -> Dict:
        """
        Perform comprehensive audit of content for all manipulation types.

        Args:
            content_data: All available content information
            user_profile: Optional user vulnerability profile

        Returns:
            Complete audit report with all findings
        """
        report = {
            'audit_timestamp': time.time(),
            'overall_risk_score': 0.0,
            'manipulation_categories': {},
            'specific_findings': [],
            'vulnerability_assessment': None,
            'regulatory_concerns': [],
            'recommended_interventions': [],
            'summary': ''
        }

        risk_scores = []

        # 1. Multimodal analysis (if audio/video present)
        if 'audio' in content_data or 'video' in content_data:
            if 'audio' in content_data:
                audio_result = self.multimodal_detector.analyze_audio_features(content_data['audio'])
                report['manipulation_categories']['audio'] = {
                    'risk_score': audio_result.risk_score,
                    'manipulation_types': [t.value for t in audio_result.manipulation_types]
                }
                risk_scores.append(audio_result.risk_score)

            if 'video' in content_data:
                video_result = self.multimodal_detector.analyze_video_features(content_data['video'])
                report['manipulation_categories']['video'] = {
                    'risk_score': video_result.risk_score,
                    'manipulation_types': [t.value for t in video_result.manipulation_types]
                }
                risk_scores.append(video_result.risk_score)

        # 2. Text/message analysis
        if 'text' in content_data or 'messages' in content_data:
            text = content_data.get('text', '')
            messages = content_data.get('messages', [])

            # Trust exploitation
            trust_indicators = self.trust_detector.analyze_message(text)
            if trust_indicators:
                report['manipulation_categories']['trust_exploitation'] = {
                    'indicators': [ind.exploitation_type.value for ind in trust_indicators],
                    'risk_level': max(ind.risk_level for ind in trust_indicators)
                }
                risk_scores.append(0.7 if 'critical' in [ind.risk_level for ind in trust_indicators] else 0.4)

            # Grooming patterns (if messages)
            if messages:
                grooming_result = self.grooming_detector.analyze_interaction_sequence(messages)
                if grooming_result.risk_score > 0.3:
                    report['manipulation_categories']['grooming_patterns'] = {
                        'stage': grooming_result.stage,
                        'risk_score': grooming_result.risk_score
                    }
                    risk_scores.append(grooming_result.risk_score)

            # AI-generated content check
            ai_result = self.ai_detector.analyze_text_for_ai_generation(text)
            if ai_result.ai_generated_probability > 0.4:
                report['manipulation_categories']['ai_generated'] = {
                    'probability': ai_result.ai_generated_probability,
                    'markers': ai_result.synthetic_markers
                }
                risk_scores.append(ai_result.ai_generated_probability * 0.5)

        # 3. Platform/interface analysis
        if 'interface' in content_data:
            platform_result = self.platform_detector.analyze_app_interface(content_data['interface'])
            if platform_result.overall_manipulation_score > 0.3:
                report['manipulation_categories']['platform_manipulation'] = {
                    'types': [t.value for t in platform_result.manipulation_types],
                    'risk_score': platform_result.overall_manipulation_score
                }
                risk_scores.append(platform_result.overall_manipulation_score)

        # 4. Pricing analysis
        if 'pricing' in content_data:
            pricing_result = self.economic_detector.analyze_pricing_page(content_data['pricing'])
            if pricing_result.overall_manipulation_score > 0.3:
                report['manipulation_categories']['economic_manipulation'] = {
                    'types': [t.value for t in pricing_result.manipulation_types],
                    'risk_score': pricing_result.overall_manipulation_score
                }
                risk_scores.append(pricing_result.overall_manipulation_score)

        # 5. Vulnerability assessment
        if user_profile:
            vuln_profile = self.vulnerability_detector.assess_individual_vulnerability(user_profile)
            report['vulnerability_assessment'] = {
                'score': vuln_profile.overall_vulnerability_score,
                'factors': [f.value for f in vuln_profile.factors],
                'risk_areas': vuln_profile.exploitation_risk_areas,
                'recommendations': vuln_profile.protective_recommendations
            }

            # Adjust overall risk based on vulnerability
            if vuln_profile.overall_vulnerability_score > 0.5:
                risk_scores = [r * 1.3 for r in risk_scores]

        # Calculate overall risk
        if risk_scores:
            report['overall_risk_score'] = min(1.0, np.mean(risk_scores) + np.max(risk_scores) * 0.2)

        # 6. Regulatory compliance check
        manipulation_summary = {
            'manipulation_types': list(report['manipulation_categories'].keys()),
            'overall_risk_score': report['overall_risk_score']
        }
        violations = self.compliance_analyzer.analyze_compliance(manipulation_summary)
        if violations:
            report['regulatory_concerns'] = [
                {
                    'law': v.specific_law,
                    'severity': v.severity,
                    'remediation': v.remediation_steps
                }
                for v in violations
            ]

        # 7. Intervention recommendations
        report['recommended_interventions'] = self.intervention_analyzer.recommend_interventions(
            manipulation_summary,
            user_profile
        )

        # 8. Generate summary
        report['summary'] = self._generate_summary(report)

        return report

    def _generate_summary(self, report: Dict) -> str:
        """Generate human-readable summary"""
        risk_level = 'HIGH' if report['overall_risk_score'] > 0.7 else (
            'MEDIUM' if report['overall_risk_score'] > 0.4 else 'LOW'
        )

        categories = list(report['manipulation_categories'].keys())

        summary_parts = [
            f"Overall Risk Level: {risk_level} ({report['overall_risk_score']:.2f})",
            f"Manipulation Categories Detected: {len(categories)}"
        ]

        if categories:
            summary_parts.append(f"Types: {', '.join(categories)}")

        if report['regulatory_concerns']:
            summary_parts.append(f"Regulatory Concerns: {len(report['regulatory_concerns'])} potential violations")

        if report['vulnerability_assessment']:
            vuln_score = report['vulnerability_assessment']['score']
            summary_parts.append(f"User Vulnerability: {'HIGH' if vuln_score > 0.6 else 'MODERATE' if vuln_score > 0.3 else 'LOW'}")

        return ' | '.join(summary_parts)


# Import statement for using all detectors
import time

# Example usage
if __name__ == "__main__":
    auditor = ComprehensivePersuasionAuditor()

    # Example audit
    sample_content = {
        'text': 'Act now! Limited time offer expires in 24 hours. Our experts recommend this product.',
        'interface': {
            'features': ['streak counter', 'daily rewards', 'leaderboard'],
            'signup_steps': 2,
            'cancel_steps': 8,
            'cancel_requirements': ['call to cancel', 'survey required'],
            'reward_schedule': 'variable'
        },
        'pricing': {
            'prices': [
                {'name': 'Basic', 'displayed_price': 9.99},
                {'name': 'Pro', 'displayed_price': 19.99},
                {'name': 'Enterprise', 'displayed_price': 24.99}
            ],
            'original_prices': [19.99, 39.99, 49.99],
            'urgency_elements': ['Only 3 left in stock!', 'Sale ends in 2:34:21']
        }
    }

    sample_user = {
        'age': 72,
        'cognitive_indicators': ['processing_speed_decline'],
        'emotional_state': 'loneliness',
        'social_connection_score': 0.2,
        'digital_literacy_score': 0.3
    }

    result = auditor.full_audit(sample_content, sample_user)
    print(result['summary'])
```

---

## APPENDIX: RESEARCH SOURCES

See [APPENDIX_RESEARCH_SOURCES.md](./APPENDIX_RESEARCH_SOURCES.md) for complete academic citations and regulatory references.

### Additional 2024-2025 Sources Used in This Document

**Multimodal & Audio:**
- ICMI 2025: Multimodal persuasion research
- Personality and Social Psychology Bulletin 2024: Voice tone and persuasion
- MDPI 2024: ASMR emotional and physiological responses

**Social Networks:**
- Springer 2025: Cascading falsehoods mapping
- Nature 2026: Temporal graph analysis of fake news
- Frontiers 2025: Misinformation spread modeling
- NATO StratCom 2024: Social media manipulation report

**Trust & Grooming:**
- ACIG Journal 2024: Trust framework for cybersecurity
- Zero Abuse Project 2024: Manipulation and grooming patterns

**Platform Mechanics:**
- CHI 2024: "Staying at the Roach Motel"
- CHI 2025: Design frictions on social media
- ScienceDirect 2025: Scroll immersion research

**Vulnerable Populations:**
- USC Dornsife 2024: Alzheimer's and scam vulnerability
- PNAS Nexus 2024: APOE4 and phishing
- Thorn 2024: Youth online safety data
- Psychology Today 2025: Neurodivergent vulnerability

**AI & Deepfakes:**
- Science 2025: Political persuasion with AI
- Nature 2025: LLM persuasive power meta-analysis
- PMC 2025: Deepfake forensics survey
- Deloitte 2025: Deepfake disruption report

**Interventions:**
- Sage 2024: Media literacy meta-analysis (N=81,155)
- Taiwan 2024: Adolescent media literacy intervention

**Regulatory:**
- FTC 2024: Amazon, Adobe enforcement actions
- EU DSA 2024: Implementation and enforcement

