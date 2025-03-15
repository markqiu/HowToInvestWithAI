"""
How to use personal access token to init Coze client.
"""

# Firstly, you need to access https://www.coze.com/open/oauth/pats (for the cn environment,
# visit https://www.coze.cn/open/oauth/pats).
#
# Click to add a new token. After setting the appropriate name, expiration time, and
# permissions, click OK to generate your personal access token. Please store it in a
# secure environment to prevent this personal access token from being disclosed.

import os
from dotenv import load_dotenv
load_dotenv()

import os
from cozepy import Coze, TokenAuth, COZE_CN_BASE_URL

# 通过环境变量引入密钥，访问 coze.cn 服务​
coze = Coze(auth=TokenAuth(os.getenv("COZE_API_TOKEN")), base_url=COZE_CN_BASE_URL)

