start_price_old, start_price_new, saving_per_month, percent_loss_by_month=2000, 8000, 1000, 1.5
start_diff = start_price_new - start_price_old
current_save = saving_per_month
current_loss = percent_loss_by_month
for i in range(20):
    if i % 2 ==0:
        start_diff = start_diff * (1 - current_loss / 100)
    else:
        current_loss += 0.5
        start_diff = start_diff * (1 - current_loss / 100)
    diff = start_diff - current_save
    current_save += saving_per_month
    if diff <0:
        print([i+1,abs(int(diff))])
        break
