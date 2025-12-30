# config.py
# ここに設定を記載します

import os
from dotenv import load_dotenv

load_dotenv()

# --- Base Model Definitions ---
# 基本となるモデル定義（環境変数で上書き可能）
MODEL_FAST = os.getenv("MODEL_FAST", "gpt-4o-mini") # 速度・コスト重視
MODEL_SMART = os.getenv("MODEL_SMART", "gpt-4o")    # 品質・推論能力重視

# --- Task Specific Model Assignments ---
# 利用タイミングごとのモデル割り当て

# 1. Webコンテンツフィルタリング (速度重視)
MODEL_CAPTURE_FILTERING = MODEL_FAST

# 2. Hot Cache / サジェスト生成 (速度重視)
MODEL_HOT_CACHE = MODEL_FAST

# 3. 意図判定・ルーティング (速度重視)
MODEL_INTENT_ROUTING = MODEL_FAST

# 4. 興味の探索・チャット (速度重視 - テンポ優先)
MODEL_INTEREST_EXPLORATION = MODEL_FAST

# 5. 状況分析・事実抽出 (品質重視 - 文脈理解必須)
MODEL_SITUATION_ANALYSIS = MODEL_SMART

# 6. 仮説生成 (品質重視 - 洞察力必須)
MODEL_HYPOTHESIS_GENERATION = MODEL_SMART

# 7. 構造分析・グラフ化 (品質重視 - 論理整合性必須)
MODEL_STRUCTURAL_ANALYSIS = MODEL_SMART

# 8. イノベーション・結合 (品質重視 - 創造性必須)
MODEL_INNOVATION_SYNTHESIS = MODEL_SMART

# 9. ギャップ分析 (品質重視 - 批判的思考必須)
MODEL_GAP_ANALYSIS = MODEL_SMART

# 10. レポート生成 (品質重視 - 文章力必須)
MODEL_REPORT_GENERATION = MODEL_SMART

# 11. 応答計画 (品質重視)
MODEL_RESPONSE_PLANNING = MODEL_SMART

LLM_MODEL = os.getenv("LLM_MODEL") or "gpt-5-mini"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL") or "text-embedding-3-small"
EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION") or 1536)
AI_URL = "http://host.docker.internal:11434"

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "me")
DB_PASSWORD = os.getenv("DB_PASSWORD", "me")
DB_NAME = os.getenv("DB_NAME", "mydb")
DB_PORT = int(os.getenv("DB_PORT", 3306))
