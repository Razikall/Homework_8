from collections import defaultdict


class ParserProcess:

    def process_count(self, lines):
        return len(lines)

    def get_users(self, lines):
        users = []
        for line in lines:
            if line[0] not in users:
                users.append(line[0])
        return users

    def user_process_count(self, lines):
        process_user = defaultdict(int)
        for line in lines:
            user = line[0]
            process_user[user] += 1
        return process_user

    def calculate_memory_and_cpu(self, lines):
        memory_result = 0
        cpu_result = 0
        for line in lines:
            memory_number = float(line[3])
            cpu_number = float(line[2])
            memory_result += memory_number
            cpu_result += cpu_number
        return (round(memory_result, 2), round(cpu_result, 2))

    def high_cpu_process(self, lines):
        high_memory = 0
        high_cpu = 0
        high_memory_name = ""
        high_cpu_name = ""
        for line in lines:
            if float(line[3]) > high_memory:
                high_memory = float(line[3])
                high_memory_name = line[10][:23]
            elif float(line[2]) > high_cpu:
                high_cpu = float(line[2])
                high_cpu_name = line[10][:23]
        return (high_memory_name, high_cpu_name)
