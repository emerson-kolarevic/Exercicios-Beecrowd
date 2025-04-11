h_inicio, m_inicio, h_fim, m_fim = map(int, input().split())

if h_inicio == h_fim and m_inicio == m_fim:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif h_inicio == h_fim and m_inicio < m_fim:
    tempo_jogo = m_fim - m_inicio
    print(f"O JOGO DUROU 0 HORA(S) E {tempo_jogo} MINUTO(S)")

elif h_inicio < h_fim and m_inicio == m_fim:
    tempo_jogo = h_fim - h_inicio
    print(f"O JOGO DUROU {tempo_jogo} HORA(S) E 0 MINUTO(S)")

elif h_inicio == h_fim and m_inicio > m_fim:
    tempo_jogo = 60 - (m_inicio - m_fim)
    print(f"O JOGO DUROU 23 HORA(S) E {tempo_jogo} MINUTO(S)")

elif h_inicio < h_fim and m_inicio > m_fim:
    hora_jogo = (h_fim - h_inicio) - 1
    minuto_jogo = 60 - (m_inicio - m_fim)
    print(f"O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)")

elif (h_fim - h_inicio) == 1 and m_inicio > m_fim:
    tempo_jogo = 60 - (m_inicio - m_fim)
    print(f"O JOGO DUROU 0 HORA(S) E {tempo_jogo} MINUTO(S)")

elif h_inicio < h_fim and m_inicio < m_fim:
    hora_jogo = h_fim - h_inicio
    minuto_jogo = m_fim - m_inicio
    print(f"O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)")

elif h_inicio > h_fim and m_inicio < m_fim:
    hora_jogo = 24 - (h_inicio - h_fim) - 1
    minuto_jogo = m_fim - m_inicio
    print(f"O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)")

elif h_inicio > h_fim and m_inicio > m_fim:
    hora_jogo = 24 - (h_inicio - h_fim) - 1
    minuto_jogo = 60 - (m_inicio - m_fim)
    print(f"O JOGO DUROU {hora_jogo} HORA(S) E {minuto_jogo} MINUTO(S)")

