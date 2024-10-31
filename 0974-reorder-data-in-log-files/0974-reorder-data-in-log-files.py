class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            log_list = log.split(' ')
            parsed_log = (log_list[0], " ".join(log_list[1:]))
            if parsed_log[1].replace(' ','').isdigit():
                digit_logs.append(parsed_log)
            else:
                letter_logs.append(parsed_log)
        
        letter_logs.sort(key = lambda x:(x[1],x[0]))

        sorted_logs = letter_logs + digit_logs
        return [ " ".join(sorted_log) for sorted_log in sorted_logs]