def solution(sequence):
    answer = 0
    n = len(sequence)
    p_sequence , m_sequence = [1]*n , [1]*n  
    for i in range(n):
        if i%2:
            p_sequence[i] = -sequence[i]
            m_sequence[i] = sequence[i]
        else:
            p_sequence[i] = sequence[i]
            m_sequence[i] = -sequence[i]
    m_data,p_data = [0]*(1+n),[0]*(1+n)
    m_data[1],p_data[1]= m_sequence[0],p_data[0]
    for i in range(1,n+1):
        m_data[i] = max(m_sequence[i-1],m_sequence[i-1] + m_data[i-1])
        p_data[i] = max(p_sequence[i-1],p_sequence[i-1] + p_data[i-1])
    for i in range(n+1):
        answer = max(answer,m_data[i],p_data[i])
    return answer
