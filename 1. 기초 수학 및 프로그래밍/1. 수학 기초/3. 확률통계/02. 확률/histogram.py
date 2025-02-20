import matplotlib.pyplot as plt


def count_freq(data):
    data_freq = {}
    keys = list(set(data))
    keys.sort()
    for key in keys:
        data_freq[key] = 0
    for value in data:
        data_freq[value] += 1
    return data_freq


def freq2ratio(dic):
    n = sum(dic.values())
    res = {}
    for key in dic.keys():
        val = dic[key]
        res[key] = val / n
    return res


data = [1, 3, 3, 2, 3, 4, 2, 4, 5, 3]
data_freq = count_freq(data)
print(data_freq)

data_ratio = freq2ratio(data_freq)
print(data_ratio)

plt.hist(data, bins=5, color='green')
plt.show()