### Висновки щодо швидкостей алгоритмів

#### Article 1

| Substring               | Boyer-Moore | KMP        | Rabin-Karp |
|-------------------------|-------------|------------|------------|
| відомі алгоритми пошуку | 0.00028588  | 0.00369412 | 0.00548575 |
| випадковий підрядок     | 0.00027929  | 0.00371721 | 0.00543179 |

- **Boyer-Moore**:
    - Для підрядка "відомі алгоритми пошуку": 0.00028588 секунд.
    - Для підрядка "випадковий підрядок": 0.00027929 секунд.
    - Цей алгоритм демонструє найшвидшу роботу серед усіх трьох для обох підрядків у тексті Article 1.

- **Кнута-Морріса-Пратта (KMP)**:
    - Для підрядка "відомі алгоритми пошуку": 0.00369412 секунд.
    - Для підрядка "випадковий підрядок": 0.00371721 секунд.
    - KMP алгоритм є повільнішим порівняно з Boyer-Moore, але все ще показує стабільний час виконання.

- **Рабіна-Карпа**:
    - Для підрядка "відомі алгоритми пошуку": 0.00548575 секунд.
    - Для підрядка "випадковий підрядок": 0.00543179 секунд.
    - Алгоритм Рабіна-Карпа є найповільнішим серед усіх трьох для обох підрядків у тексті Article 1.

#### Article 2

| Substring               | Boyer-Moore | KMP        | Rabin-Karp |
|-------------------------|-------------|------------|------------|
| відомі алгоритми пошуку | 0.00038700  | 0.00549104 | 0.00802329 |
| випадковий підрядок     | 0.00042017  | 0.00550408 | 0.00796687 |

- **Boyer-Moore**:
    - Для підрядка "відомі алгоритми пошуку": 0.00038700 секунд.
    - Для підрядка "випадковий підрядок": 0.00042017 секунд.
    - Як і в Article 1, Boyer-Moore алгоритм показує найкращу продуктивність для обох типів підрядків у тексті Article
      2.

- **Кнута-Морріса-Пратта (KMP)**:
    - Для підрядка "відомі алгоритми пошуку": 0.00549104 секунд.
    - Для підрядка "випадковий підрядок": 0.00550408 секунд.
    - KMP алгоритм є повільнішим за Boyer-Moore, але його продуктивність залишається стабільною для обох підрядків.

- **Рабіна-Карпа**:
    - Для підрядка "відомі алгоритми пошуку": 0.00802329 секунд.
    - Для підрядка "випадковий підрядок": 0.00796687 секунд.
    - Рабін-Карп алгоритм є найповільнішим для обох підрядків у тексті Article 2.

### Загальний висновок

- **Boyer-Moore** алгоритм показав найкращу продуктивність для обох типів підрядків в обох статтях. Це свідчить про те,
  що Boyer-Moore є найбільш ефективним серед трьох розглянутих алгоритмів для цих текстів.

- **Кнута-Морріса-Пратта (KMP)** алгоритм демонструє стабільну, але дещо повільнішу продуктивність порівняно з
  Boyer-Moore. Однак він є кращим за Рабін-Карп у всіх випадках.

- **Рабіна-Карпа** алгоритм є найповільнішим серед трьох для обох підрядків і в обох статтях. Це свідчить про те, що він
  менш ефективний для пошуку підрядків у цих текстах.