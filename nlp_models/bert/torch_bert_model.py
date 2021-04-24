# Requirements
# Python 3.6+
# Torch 1.8+

class BertClassifier(nn.Module):

  def __init__(self, n):

    super(BertClassifier, self).__init__()
    self.bert = BertModel.from_pretrained('bert-base-cased')
    self.drop = nn.Dropout(p=0.3)
    self.out = nn.Linear(self.bert.config.hidden_size, n)

  def forward(self, input_ids, attention_mask):

    _, pooled_output = self.bert(
      input_ids=input_ids,
      attention_mask=attention_mask,
      return_dict=False)
    output = self.drop(pooled_output)

    return self.out(output)