import json
import gzip
import os
from RWV.pushshift.classes import Post, Comment


class Content:
    """ For loading saved files."""

    def __init__(self, file_name):
        if '.json.gz' not in file_name:
            file_name += '.json.gz'

        self.file_name = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/reddit_data/' + file_name)
        self.data = None

    def load_content_from_file(self):
        """ Loads saved .json.gz file as is. """
        with gzip.GzipFile(self.file_name) as f:
            json_bytes = f.read()

        json_str = json_bytes.decode('utf-8')
        self.data = json.loads(json_str)

        return self

    def load_posts(self):
        """ Loads posts as list of Post objects. """
        self.load_content_from_file()

        post_object_lst = []

        for post in self.data:
            post_object_lst.append(Post.make_post_obj(post))

        return post_object_lst

    def load_comments(self):
        """ Loads comments as list of Comment objects. """
        self.load_content_from_file()

        comment_object_lst = []

        for comment in self.data:
            comment_object_lst.append(Comment.make_comment_obj(comment))

        return comment_object_lst
