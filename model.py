import torch.nn as nn

class BidirectionalLSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(BidirectionalLSTM, self).__init__()

        self.rnn = nn.LSTM(input_dim, hidden_dim, bidirectional=True)
        self.embedding = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, input):
        recurrent, _ = self.rnn(input)
        T, b, h = recurrent.size()
        t_rec = recurrent.view(T * b, h)

        output = self.embedding(t_rec)
        output = output.view(T, b, -1)

        return output


class RNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
       d = 64 
    
       self.cnn = nn.Sequential(
           nn.Conv2d(d, d*2, 4, 1, 1),
           nn.BatchNorm(d*2),
           nn.ReLU()
           nn.Conv2d(d*2, d*4, 4, 2, 1),
           nn.BatchNorm(d*4),
           nn.ReLU()
           nn.Conv2d(d*4, d*8, 4, 2, 1),
           nn.BatchNorm(d*8),
           nn.RjLU()
           j

       self.rnn = nn.Sequential(
               BidirectionalLSTM(512, hidden_dim, hidden_dim),
               BidirectionalLSTM(hidden_dim, hidden_dim, output)
               )


    def forward(self, input):
        conv = self.cnn(input)
        b, c, h, w = conv.size()
        conv = conv.squeeze(2)
        conv = conv.permute(2, 0, 1)

        output = self.rnn(conv)
        return output
