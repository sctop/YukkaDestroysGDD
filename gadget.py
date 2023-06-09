import csv
import hashlib


class ChatContent:
    def __init__(self, content: str):
        content = content.split(",")
        self._author, self._date, self._author_name, self._role, self._message, self._video_time, self._id = \
            content[0], content[1], content[2], content[3], content[4], content[5], content[6]

    def get_md5(self):
        return hashlib.md5(bytes(self._id + self._message, encoding="UTF-8")).hexdigest()

    def to_csv(self):
        temp = [self._author, self._date, self._author_name, self._role, self._message, self._video_time, self._id]
        return ",".join(temp)

    def to_json(self):
        return {"author": self._author, "date": self._date, "author_name": self._author_name,
                "role": self._role, "message": self._message, "video_time": self._video_time, "id": self._id,
                "hash": str(hex(hash(self)))}

    @property
    def author(self):
        return self._author

    @property
    def date(self):
        return self._date

    @property
    def author_name(self):
        return self._author_name

    @property
    def role(self):
        return self._role

    @property
    def message(self):
        return self._message

    @property
    def video_time(self):
        return self._video_time

    @property
    def id(self):
        return self._id


class HashlibBasedList():
    def __init__(self):
        super().__init__()
        self.md5_dict = {}
        self.item_list: [ChatContent, ...] = []

    def append(self, item) -> None:
        item_md5 = item.get_md5()
        if item_md5 not in self.md5_dict:
            self.md5_dict[item_md5] = item
            self.item_list.append(item)

    def remove(self, md5):
        self.item_list.remove(self.md5_dict[md5])
        del self.md5_dict[md5]

    def get_items(self) -> list:
        return self.item_list

    def __iter__(self):
        return iter(self.item_list)

    def __getitem__(self, item):
        return self.item_list[item]

    def __len__(self):
        return len(self.item_list)


def read_csv(filename):
    with open(filename, mode="r", encoding="gbk") as csv_file:
        reader = csv.reader(csv_file)
        line_num = 0
        for row in reader:
            if line_num == 0:
                yield row
            else:
                yield ChatContent(",".join(row))
            line_num += 1
