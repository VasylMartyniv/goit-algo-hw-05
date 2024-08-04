import timeit

import chardet
from prettytable import PrettyTable


def read_file(filename):
    with open(filename, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open(filename, 'r', encoding=encoding) as file:
        return file.read()


def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    skip = {}
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1

    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m)
    return -1


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0

    def compute_lps(pattern):
        length = 0
        lps[0] = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    compute_lps(pattern)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern):
    d = 256
    q = 101
    n = len(text)
    m = len(pattern)
    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q
    return -1


article1 = read_file('article1.txt')
article2 = read_file('article2.txt')

existing_substring = "відомі алгоритми пошуку"
non_existing_substring = "випадковий підрядок"

algorithms = {
    "Boyer-Moore": boyer_moore,
    "KMP": kmp,
    "Rabin-Karp": rabin_karp
}


def measure_time(algorithm, text, pattern):
    timer = timeit.Timer(lambda: algorithm(text, pattern))
    return timer.timeit(number=1)


def create_table(results, substrings, title):
    table = PrettyTable()
    table.field_names = ["Substring"] + list(results.keys())

    for substring in substrings:
        row = [substring]
        for algorithm in results:
            row.append(f"{results[algorithm][substring]:.8f}")
        table.add_row(row)

    table.title = title
    return table


results_article1 = {name: {} for name in algorithms}
for name, algorithm in algorithms.items():
    results_article1[name][existing_substring] = measure_time(algorithm, article1, existing_substring)
    results_article1[name][non_existing_substring] = measure_time(algorithm, article1, non_existing_substring)

results_article2 = {name: {} for name in algorithms}
for name, algorithm in algorithms.items():
    results_article2[name][existing_substring] = measure_time(algorithm, article2, existing_substring)
    results_article2[name][non_existing_substring] = measure_time(algorithm, article2, non_existing_substring)

substrings = [existing_substring, non_existing_substring]

table1 = create_table(results_article1, substrings, "Article 1")
table2 = create_table(results_article2, substrings, "Article 2")

print(table1)
print(table2)
