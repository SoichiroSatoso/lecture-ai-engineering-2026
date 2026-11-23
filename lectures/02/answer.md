# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
```
"config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
```

- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` =　 0.09523809523809523 / `content_rate` =　0.0
- 学習後：`format_rate` =　0.09523809523809523 / `content_rate` =　0.9047619047619048
- 退行した質問：
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：根拠なしの質問に断定した
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：学習したデータに含まれない知識は学習できない
- 学習で変わったこと・変わらなかったこと：特定の答え方と出力の形式を学習できているところが変わったところである。変わっていないところは学習データにない知識は答えられないことと。

## 宿題

- 取り組んだレベル：実装 
- 変えた設定やデータ：データを変えた。FAQを以下に変えて、ほかデータも対応したものにした。
```
FAQ = {
    "abstract": "llmの学習をしています。LoRAを試しています。",
    "funny": "AIの勉強をするのは楽しいです",
    "can_do": "勉強することでAIができることとできないことがわかる",
    "interest": "学習の方法とフローに興味がある。",
}
```

- 結果（比較表や数字）：
```
{
  "config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  },
  "versions": {
    "transformers": "5.18.0",
    "peft": "0.21.1",
    "trl": "1.14.2",
    "torch": "2.11.0+cu130"
  },
  "method": "LoRA（量子化なし）",
  "before": {
    "label": "before",
    "n": 23,
    "format_rate": 0.34782608695652173,
    "content_rate": 0.21739130434782608,
    "both_rate": 0.21739130434782608,
    "seconds": 59.3
  },
  "after": {
    "label": "after",
    "n": 23,
    "format_rate": 1.0,
    "content_rate": 0.6956521739130435,
    "both_rate": 0.6956521739130435,
    "seconds": 31.6
  },
  "regressed": [
    "AIの勉強には毎日何時間使っていますか？"
  ],
  "executed_training_myself": true
}
```

- ファインチューニングが向く場面・向かない場面についての考察：出力の形式を覚えさせたいときにはとても有用である。とくに返答で出力したいパターンがいくつかに決まっているときに有用に思える。ただ誤検出が多く、関係ない質問を判別する能力はつきにくいように感じた。返答に精密な判断をさせたい場合にはファインチューニングだけでは足りないと感じた。