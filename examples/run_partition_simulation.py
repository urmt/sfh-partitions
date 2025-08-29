from partitions import partition_info

for Q in range(1, 21):
    info = partition_info(Q)
    print(f"Q={Q}, exact={info['exact']}, approx={info['asymptotic']:.2f}, forbidden={info['forbidden']}")
