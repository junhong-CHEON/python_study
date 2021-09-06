from sklearn.model_selection import KFold


# 데이터셋 분할 후 k폴드 적용
# ----------------------------------------------------
# # 분할할 그룹(=폴드) 수
k = 3

kfold = KFold(n_splits=k)

# 표준화 한 훈련 데이터를 k개 만큼 분할
split_x_train = list(kfold.split(x_train))

for i in range(0, len(split_x_train)):
    print("[%d번째 폴드의 인덱스]" % i)
    print("=" * 50)
    print("Train-set: \t%s" % split_x_train[i][0])
    print("-" * 50)
    print("Test-set: \t%s" % split_x_train[i][1])
    print("=" * 50)
    print()

# 교차검증 적용 분석
# =====================================================
# 테스트 셋을 평가한 후 결과를 저장할 리스트
result_list = []
model_list = []

for i, v in enumerate(split_x_train):
    print("[%d번째 폴드]" % i)

    x_train_fold = x_train[x_train.index[v[0]]]
    x_test_fold = x_train[x_train.index[v[1]]]
    y_train_fold = y_train[y_train.index[v[0]]]
    y_test_fold = y_train[y_train.index[v[1]]]

    # 데이터가 단순하고 개수가 적다면 과대적합이 발생할 확률이 높기 때문에 주의하면서 적절한 크기의 모델층을 쌓아야 한다.
    model = Sequential()
    # 1차원의 데이터를 입력으로 받고, 64개의 출력을 가지는 첫 번째 Dense 층
    model.add(Dense(32, activation = 'relu', input_shape = (1, )))
    # 하나의 값을 출력
    # -> 정답의 범위가 정해지지 않기 때문에 활성화 함수는 linear
    # -> linear는 기본값이므로 생략 가능함.
    model.add(Dense(1, activation='linear'))

    model.compile(optimizer = 'adam', loss = 'mse', metrics = ['mae'])
    model.summary()

    result = model.fit(x_train_fold, y_train_fold, epochs=300, validation_data=(x_test_fold, y_test_fold), callbacks = [
         EarlyStopping(monitor = 'val_loss', patience=5, verbose = 1),
         ReduceLROnPlateau(monitor= "val_loss", patience=3, factor = 0.5, min_lr=0.0001, verbose=2),
         ModelCheckpoint(filepath = 'cars_var_loss.h5', monitor = 'val_loss', verbose=2, save_best_only = True)
    ])

    result_list.append(result)
    model_list.append(model)

result_list
