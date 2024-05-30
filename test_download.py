from huggingface_hub import snapshot_download
from huggingface_hub import login

login("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")
snapshot_download(
  #repo_id="baichuan-inc/Baichuan2-13B-Chat",
  #repo_id="BAAI/bge-m3",
  repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
  local_dir="./",
  #proxies={"https": "http://localhost:7890"},
  max_workers=1
)
