notas = [5, 7, 5, 4, 8]
notasBuenas = [nota for nota in notas if nota > 7]
# print(notasBuenas)

nums = [4, -5, 7, -1, 0]
cantNegativos = [sum(num > 0 for num in nums)]
# print(cantNegativos)

buls = [False, False, False, False, True]


# print(sum(buls))

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    #return [sum(meals.index(meals[m]) == meals.index(meals[m+1]) for m in range(len(meals)-1))>0]
    return any(meals.index(meals[m]) == meals.index(meals[m + 1]) for m in range(len(meals) - 1))


#print(menu_is_boring(['a', 'b', 'b']))
def play_slot_machine():
    return 4

def estimate_average_slot_payout(n_runs):

    return [sum(play_slot_machine() for n in range(n_runs))]

print(estimate_average_slot_payout(5))
