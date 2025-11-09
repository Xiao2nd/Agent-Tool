import requests
import json

def test_ollama(prompt: str):
    """測試 /ollama 端點"""
    url = "http://localhost:8080/ollama"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": prompt}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"✅ 請求成功！")
        print(f"\n📝 回應內容：\n{response.text}")
    else:
        print(f"❌ 請求失敗！狀態碼：{response.status_code}")
        print(f"錯誤訊息：{response.text}")

if __name__ == "__main__":
    # 測試中文對話
    test_ollama("早安")
