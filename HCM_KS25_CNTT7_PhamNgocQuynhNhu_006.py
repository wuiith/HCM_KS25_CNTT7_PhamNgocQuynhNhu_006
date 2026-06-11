rent_list = []

def show_list():
    if not rent_list:
        print('Hiện tại danh sách đặt phòng đang trống!')
    else:
        print('\n--- THÔNG TIN DANH SÁCH ĐẶT PHÒNG ---')
        print('-'*85)
        print(f'{'Booking ID':<5} | {'Tên phòng họp đăng ký':<15} | {'Tên người/Phòng ban đặt':<15} | {'Giờ bắt đầu sử dụng':<3} | {'Giờ kết thúc sử dụng (Mốc giờ 24h)':<3} | {'Tổng thời lượng sử dụng (Giờ)':<3} | {'Phân loại khung thời gian'}')
        print('-'*85)
        for room in rent_list:
            print(f'{room['id']:<5} | {room['name_sign_in']:<15} | {room['name_user']:<15} | {room['time_start']:<3} | {room['time_end']:<3} | {room['total_time']:<3} | {room['status']} ')
        print('-'*85)


def book_new_room():
    while True:
        check_empty = False
        id = input('Nhập mã định danh lượt đặt (Booking ID): ').strip().upper()
        if id == '':
            print('Mã định danh không được bỏ trống! Vui lòng nhập lại')
            check_empty = True
            continue
        
        if not check_empty:
            break
    
    while True: 
        check_empty = False
        name_sign_in = input('Nhập tên phòng đăng ký: ').strip().title()
        if name_sign_in == '':
            print('Tên phòng đăng ký không được bỏ trống! Vui lòng nhập lại')
            check_empty = True
            continue
        
        if not check_empty:
            break
    
    while True:
        check_empty = False
        name_user = input('Nhập tên người/phòng ban đặt: ').strip().title()
        if name_user == '':
            print('Tên người/phòng ban đặt không được bỏ trống! Vui lòng nhập lại')
            check_empty = True
            continue
        
        if not check_empty:
            break
    
    while True:
        check_empty = False
        time_start = input('Nhập thời gian bắt đầu sử dụng: ')
        if time_start == '':
            print('Thời gian bắt đầu sử dụng không được bỏ trống! Vui lòng nhập lại')
            check_empty = True
            continue
        
        if not time_start.isdigit():
            print('Bạn phải nhập số nguyên!')
            continue

        if int(time_start) < 0 and int(time_start) > 24:
            print('Số giờ phải từ 1h-24h')
            continue

        if not check_empty:
            break
        
        
    while True:
        check_empty = False
        time_end = input('Nhập thời gian sử dụng kết thúc: ')
        if time_end == '':
            print('Thời gian sử dụng kết thúc không được bỏ trống! Vui lòng nhập lại')
            check_empty = True
            continue

        if not time_end.isdigit():
            print('Bạn phải nhập số nguyên!')
            continue

        if int(time_end) < 0 and int(time_end) > 24:
                print('Số giờ phải từ 1h-24h')
                continue

        if int(time_end) < int(time_start):
            print('Thời gian kết thúc không thể sớm hơn thời gian bắt đầu!')
            continue

        if not check_empty:
            break
        
    total_time = int(time_end) - int(time_start)
    
    if total_time < 2:
        status = 'Ngắn'
    elif total_time >= 2 and total_time < 4:
        status = 'Tiêu chuẩn'
    elif total_time >= 4 and total_time < 6:
        status = 'Dài'
    else:
        status = 'Quá tải (Cần xem xét lại)'


    new_booking = {
        'id' : id,
        'name_sign_in' : name_sign_in,
        'name_user' : name_user,
        'time_start' : time_start,
        'time_end' : time_end,
        'total_time' : total_time,
        'status' : status
    }

    rent_list.append(new_booking)
    print('[THÀNH CÔNG]: Đã đăng ký lịch đặt phòng mới')


def update_information_booking():
    if not rent_list:
        print('Hiện tại danh sách đặt phòng đang trống!')
    else:
        found = True
        user_id_input = input('Nhập mã định danh (Booking ID) cần gia hạn thêm giờ: ').strip().upper()
        for value in rent_list:
            if value['id'] != user_id_input:
                print('Mã đặt phòng hiện không tồn tại!')
                found = False
        
        if found:
            while True: 
                check_empty = False
                new_name_sign_in = input('Vui lòng nhập lại tên phòng đăng ký: ').strip().title()
                if new_name_sign_in == '':
                    print('Tên phòng đăng ký không được bỏ trống! Vui lòng nhập lại')
                    check_empty = True
                    continue
                
                if not check_empty:
                    break

        while True:
            check_empty = False
            new_time_start = input('Nhập thời gian bắt đầu sử dụng: ')
            if new_time_start == '':
                print('Thời gian bắt đầu sử dụng không được bỏ trống! Vui lòng nhập lại')
                check_empty = True
                continue
            
            if not new_time_start.isdigit():
                print('Bạn phải nhập số nguyên!')
                continue

            if int(new_time_start) < 0 and int(new_time_start) > 24:
                print('Số giờ phải từ 1h-24h')
                continue

            if not check_empty:
                break
        
        
        while True:
            check_empty = False
            new_time_end = input('Nhập thời gian sử dụng kết thúc: ')
            if new_time_end == '':
                print('Thời gian sử dụng kết thúc không được bỏ trống! Vui lòng nhập lại')
                check_empty = True
                continue

            if not new_time_end.isdigit():
                print('Bạn phải nhập số nguyên!')
                continue

            if int(new_time_end) < 0 and int(new_time_end) > 24:
                print('Số giờ phải từ 1h-24h')
                continue

            if int(new_time_end) < int(new_time_end):
                print('Thời gian kết thúc không thể sớm hơn thời gian bắt đầu!')
                continue

            if not check_empty:
                break
        
        new_total_time = int(new_time_end) - int(new_time_start)

    
        if new_total_time < 2:
            status = 'Ngắn'
        elif new_total_time >= 2 and new_total_time < 4:
            status = 'Tiêu chuẩn'
        elif new_total_time >= 4 and new_total_time < 6:
            status = 'Dài'
        else:
            status = 'Quá tải (Cần xem xét lại)'

        for value in rent_list:
            'name_sign_in' = new_name_sign_in
            'time_start' = new_time_start
            'time_end' = new_time_end
            'total_time' = new_total_time
            'status' = status

            
def found_room():
    if not rent_list:
        print('Hiện tại danh sách đặt phòng đang trống!')
    else:
        while True:
            print('1. Tìm kiếm dựa trên ID (chính xác theo ID)')
            print('2. Tìm kiểu gần đúng theo Tên phòng họp')
            print('3. Thoát chức năng')
            user = input('Nhập lựa chọn của bạn')

            if not user.isdigit():
                print('Bạn phải nhập vào số nguyên 1 hay 2')
                continue

            if int(user) != 1 and int(user) != 2:
                print('Bạn chỉ được phép nhập 1 hoặc 2')
                continue

            match user:
                case "1":
                    found = True
                    user_id_input = input('Nhập mã định danh (Booking ID) cần gia hạn thêm giờ: ').strip().upper()
                    for value in rent_list:
                        if value['id'] != user_id_input:
                            print('Mã đặt phòng hiện không tồn tại!')
                            found = False
                    
                    if found:
                        print('--- THÔNG TIN LỊCH ĐẶT ---')
                        print('-'*85)
                        for infor in rent_list:
                            if infor['id'] == user_id_input:
                                print(f'{infor['id']:<5} | {infor['name_sign_in']:<15} | {infor['name_user']:<15} | {infor['time_start']:<3} | {infor['time_end']:<3} | {infor['total_time']:<3} | {infor['status']} ')
                            print('-'*85)

                case "2":
                    print('--- THÔNG TIN LỊCH ĐẶT ---')
                    print('-'*85)
                    user_input = input('Nhập tên phòng họp: ').strip().lower()
                    for value in rent_list:
                        if user_input.lower() in value['name_sign_in'.lower()]:
                            for infor in rent_list:
                                print(f'{infor['id']:<5} | {infor['name_sign_in']:<15} | {infor['name_user']:<15} | {infor['time_start']:<3} | {infor['time_end']:<3} | {infor['total_time']:<3} | {infor['status']} ')
                            print('-'*85)
                        else:
                            print('Tên phòng ban không tồn tại!')
                    
                case "3":
                    print('Thoát chức năng...')
                    break



def menu():
    while True:
        print('\n------- HỆ THỐNG ĐẶT LỊCH -------')
        print('='*85)
        print('1. Hiển thị danh sách lịch đặt')
        print('2. Đăng ký lịch đặt phòng mới')
        print('3. Cập nhật thông tin lịch hẹn')
        print('4. Hủy/Xóa lịch đặt phòng')
        print('5. Tìm kiếm lịch đặt phòng')
        print('6. Thống kê mật độ sử dụng')
        print('7. Phân loại khung giờ tự động')
        print('8. Thoát chương trình')
        print('='*85)

        choice = int(input('Nhập lựa chọn của bạn: '))

        if choice == '':
            print('Không được bỏ trống lựa chọn!')
            continue
        
        match choice:
            case 1:
                show_list()

            case 2:
                book_new_room()

            case 3:
                update_information_booking()

            case 5:
                found_room()

            case 8:
                print('Thoát chương trình..')
                break
            case _:
                print('Cú pháp không hợp lệ')

menu()


