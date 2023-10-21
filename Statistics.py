class Statistics:
    def __init__(self):
        # score data
        self.highest_score = 0
        self.total_score = 0

        # entity statistics
        #   levels
        self.highest_level_achieved = 0
        self.total_levels_gained = 0

        # general statistics
        #   health
        self.most_health_recovered = 0
        self.total_health_recovered = 0

        #   damage
        self.most_damage_dealt = 0
        self.most_damage_taken = 0
        self.total_damage_dealt = 0
        self.total_damage_taken = 0

        self.total_hits = 0
        self.total_self_hits = 0
        self.crit_tracker = 0
        self.most_consecutive_crits = 0
        self.total_crits = 0

        #   other stats
        self.total_deaths = 0
        self.total_enemies_killed = 0
        self.total_money_gained = 0
        self.total_money_spent = 0
        self.most_money_spent = 0

    def add_score(self, score: int):
        self.total_score += score
        if score > self.highest_score:
            self.highest_score = score

    def add_level(self, current_level):
        self.total_levels_gained += 1
        if current_level > self.highest_level_achieved:
            self.highest_level_achieved = current_level

    def add_heal(self, amount: int):
        self.total_health_recovered += amount
        if amount > self.most_health_recovered:
            self.most_health_recovered = amount

    def add_crit(self):
        self.crit_tracker += 1
        self.total_crits += 1
        if self.crit_tracker > self.most_consecutive_crits:
            self.most_consecutive_crits = self.crit_tracker

    def add_hit(self, is_crit: bool, damage: int):
        self.total_hits += 1
        if is_crit:
            self.add_crit()
        else:
            self.crit_tracker = 0

        self.total_damage_dealt += damage
        if damage > self.most_damage_dealt:
            self.most_damage_dealt = damage

    def add_self_hit(self, damage: int):
        self.total_self_hits += 1
        self.total_damage_taken += damage
        if damage > self.total_damage_taken:
            self.most_damage_taken = damage

    def add_kill(self):
        self.total_enemies_killed += 1

    def add_death(self):
        self.total_deaths += 1

    def add_money(self, amount: int):
        self.total_money_gained += amount

    def spend_money(self, amount: int):
        print(self.total_money_spent)
        if amount > self.most_money_spent:
            self.most_money_spent = amount

    def converge(self, statistics):
        # totals
        self.total_score += statistics.total_score
        self.total_levels_gained += statistics.total_levels_gained
        self.total_health_recovered += statistics.total_health_recovered
        self.total_damage_dealt += statistics.total_damage_dealt
        self.total_damage_taken += statistics.total_damage_taken
        self.total_hits += statistics.total_hits
        self.total_self_hits += statistics.total_self_hits
        self.total_crits += statistics.total_crits
        self.total_enemies_killed += statistics.total_enemies_killed
        self.total_money_gained += statistics.total_money_gained
        self.total_money_spent += statistics.total_money_spent
        self.total_deaths += statistics.total_deaths

        # highest or most
        if statistics.highest_score > self.highest_score:
            self.highest_score = statistics.highest_score

        if statistics.highest_level_achieved > self.highest_level_achieved:
            self.highest_level_achieved = statistics.highest_level_achieved

        if statistics.most_health_recovered > self.most_health_recovered:
            self.most_health_recovered = statistics.most_health_recovered

        if statistics.most_damage_dealt > self.most_damage_dealt:
            self.most_damage_dealt = statistics.most_damage_dealt

        if statistics.most_damage_taken > self.most_damage_taken:
            self.most_damage_taken = statistics.most_damage_taken

        if statistics.most_consecutive_crits > self.most_consecutive_crits:
            self.most_consecutive_crits = statistics.most_consecutive_crits

        if statistics.most_money_spent > self.most_money_spent:
            self.most_money_spent = statistics.most_money_spent

    def jsonify(self):
        stats = {
            "totals": {
                "total score": self.total_score,
                "total levels gained": self.total_levels_gained,
                "total health recovered": self.total_health_recovered,
                "total damage dealt": self.total_damage_dealt,
                "total damage taken": self.total_damage_taken,
                "total hits": self.total_hits,
                "total self hits": self.total_self_hits,
                "total crits": self.total_crits,
                "total deaths": self.total_deaths,
                "total enemies killed": self.total_enemies_killed,
                "total money gained": self.total_money_gained,
                "total money spent": self.total_money_spent
            },
            "peaks": {
                "highest score": self.highest_score,
                "highest level achieved": self.highest_level_achieved,
                "most health recovered": self.most_health_recovered,
                "most damage dealt": self.most_damage_dealt,
                "most damage taken": self.most_damage_taken,
                "most consecutive crits": self.most_consecutive_crits,
                "most money spent": self.most_money_spent
            }
        }

        return stats

    def load_from_json(self, json_dict):
        # totals
        self.total_score = json_dict["totals"]["total score"]
        self.total_levels_gained = json_dict["totals"]["total levels gained"]
        self.total_health_recovered = json_dict["totals"]["total health recovered"]
        self.total_damage_dealt = json_dict["totals"]["total damage dealt"]
        self.total_damage_taken = json_dict["totals"]["total damage taken"]
        self.total_hits = json_dict["totals"]["total hits"]
        self.total_self_hits = json_dict["totals"]["total self hits"]
        self.total_crits = json_dict["totals"]["total crits"]
        self.total_deaths = json_dict["totals"]["total deaths"]
        self.total_enemies_killed = json_dict["totals"]["total enemies killed"]
        self.total_money_gained = json_dict["totals"]["total money gained"]
        self.total_money_spent = json_dict["totals"]["total money spent"]

        # peaks
        self.highest_score = json_dict["peaks"]["highest score"]
        self.highest_level_achieved = json_dict["peaks"]["highest level achieved"]
        self.most_health_recovered = json_dict["peaks"]["most health recovered"]
        self.most_damage_dealt = json_dict["peaks"]["most damage dealt"]
        self.most_damage_taken = json_dict["peaks"]["most damage taken"]
        self.most_consecutive_crits = json_dict["peaks"]["most consecutive crits"]
        self.most_money_spent = json_dict["peaks"]["most money spent"]
