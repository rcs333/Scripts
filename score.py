def print_accuracy(true_positive, false_negative, true_negative, false_positive):
    total_condition_positive = true_positive + false_negative
    total_condition_negative = false_positive + true_negative
    print('\tTotal condition negative = ' + str(total_condition_negative))
    print('\tTotal condiion positive = ' + str(total_condition_positive))
    print('\tTrue negative = ' + str(true_negative))
    print('\tFalse positive = ' + str(false_positive))
    print('\tTrue positive = ' + str(true_positive))
    print('\tfalse negative = ' + str(false_negative))

    if total_condition_positive and total_condition_negative != 0:
        total_population = total_condition_negative + total_condition_positive

        true_positive_rate = float(true_positive) / float(total_condition_positive)
        false_negative_rate = float(false_negative) / float(total_condition_positive)
        false_positive_rate = float(false_positive) / float(total_condition_negative)
        true_negative_rate = float(true_negative) / float(total_condition_negative)

        accuracy = (float(true_positive) + float(true_negative)) / float(total_population)
        percision = float(true_positive) / (float(true_positive) + float(false_positive))
        recall = true_positive_rate
        F1_score = 2.0 * ((percision * recall) / (percision + recall))

        print('\tTotal population = ' + str(total_population))

        print('\tTrue negative rate = ' + str(true_negative_rate))
        print('\tFalse negative rate = ' + str(false_negative_rate))
        print('\tFalse postive rate = ' + str(false_positive_rate))
        print('\tTrue positive rate = ' + str(true_positive_rate))

        print('\t\tAccuracy = ' + str(accuracy))
        print('\t\tF1 = ' + str(F1_score))
    else:
        print('Something was zero')

print('A8 Accuracy Results')
print_accuracy(21, 4, 16, 4)
print('\n')

print('AW Accuracy Results')
print_accuracy(19, 6, 24, 1)
print('\n')

print('CB Accuracy Results')
print_accuracy(21, 4, 22, 3)
print('\n')

print('D65 Accuracy Results')
print_accuracy(20, 5, 22, 3)
print('\n')

print('FCB Accuracy Results')
print_accuracy(19, 6, 19, 6)
print('\n')

print('JH Accuracy Results')
print_accuracy(6, 1, 6, 1)
print('\n')

print('FFB Accuracy Results')
print_accuracy(9, 1, 20, 5)
print('\n')
