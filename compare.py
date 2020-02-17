""" 
Given dev-labels.lst, compare two model's prediction
dev-predictions.lst and dev-probabilities.lst
and find where two predictions are inconsistent
"""

import argparse

def compare(label_path, jsonl_path,
            exp_name_1, pred_1_path, prob_1_path,
            exp_name_2, pred_2_path, prob_2_path):
    print(jsonl_path)
    labels = [int(i) for i in open(label_path).readlines()]
    qa_reader = open(jsonl_path)
    pred_1 = [int(i) for i in open(pred_1_path).readlines()]
    prob_1 = [[float(j) for j in i.split()] for i in open(prob_1_path).readlines()]
    pred_2 = [int(i) for i in open(pred_2_path).readlines()]
    prob_2 = [[float(j) for j in i.split()] for i in open(prob_2_path).readlines()]
    assert len(labels) == len(pred_1) == len(pred_2) == len(prob_1) == len(prob_2)
    
    for i in range(len(labels)):
        sample = qa_reader.readline()
        label = labels[i]
        if pred_1[i] != pred_2[i]:
            print("Disagreement on", str(i+1)+"-th sample:\n", sample.rstrip())
            print("The correct answer is", label)
            if pred_1[i] != label:
                print("Experiment " + exp_name_1 + "'s choice: " + str(pred_1[i]))
                print("\twith probabilities for each choice:", *prob_1[i])
            if pred_2[i] != label:
                print("Experiment " + exp_name_2 + "'s choice: " + str(pred_2[i]))
                print("\twith probabilities for each choice:", *prob_2[i])
        else:
            print("Agreed on", str(i+1)+"-th sample.")
        print()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--label_path", required=True)
    parser.add_argument("--exp_name_1", required=True)
    parser.add_argument("--exp_name_2", required=True)
    parser.add_argument("--pred_1_path", required=True)
    parser.add_argument("--pred_2_path", required=True)
    parser.add_argument("--prob_1_path", required=True)
    parser.add_argument("--prob_2_path", required=True)
    parser.add_argument("--jsonl_path", required=True)
    args = parser.parse_args()
    compare(args.label_path, args.jsonl_path,
            args.exp_name_1, args.pred_1_path, args.prob_1_path,
            args.exp_name_2, args.pred_2_path, args.prob_2_path)


if __name__ == "__main__":
    main()