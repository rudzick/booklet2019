#! /usr/bin/env python3

import argparse
import datetime
import html
import jinja2
import json
import os
import re
import sys
import textwrap


latex_substitutions = [
    (re.compile("([a-z])\*(innen|r|n)"), "\\1(\\2)"),
    (re.compile("„"), "\""),
    (re.compile("“"), "\""),
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r' "'), " \"`"),
    (re.compile(r'"([ .,;:])'), "\"'\\1"),
    (re.compile(r'^"'), "\"`"),
    (re.compile(r'"$'), "\"'"),
    (re.compile("([^ ]) (–|-) "), "\\1~-- ")
]

commands = {
    "Audimax S239": {
        "name": "S239",
        "command": "\\abstractAudimax"
        },
    "Mathe Z211": {
        "name": "Z211",
        "command": "\\abstractMathe"
        },
    "Physik Z254": {
        "name": "Z254",
        "command": "\\abstractPhysik"
        },
    "Recht Z208": {
        "name": "Z208",
        "command": "\\abstractRecht"
        },
    "Bärenzwinger": {
        "name": "Bärenzwinger",
        "command": "\\abstractBaerenzwinger"
        },
}
default_cmd = {"name": "???", "command": "\\abstractOther"}
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
RE_SINGLE_NEWLINE = re.compile("[^\\n]\\n", re.MULTILINE)

def datetimeformat(value, format="%H:%M"):
    return value.strftime(format)

def escape_latex(source):
    result = source
    for pair in latex_substitutions:
        result = pair[0].sub(pair[1], result)
    return result


def break_long_lines(source):
    # split source by newlines to preserve them
    splitted = source.replace("\r\n", "\n")
    splitted = RE_SINGLE_NEWLINE.sub("\\n\\n", splitted).split("\n")
    result = []
    for paragraph in splitted:
        if paragraph != "":
            result += textwrap.wrap(paragraph, 98, break_on_hyphens=False)
        else:
            # empty lines
            result.append("")
    # add two spaces at the beginning of each line
    for i in range(0, len(result)):
        if result[i] != "":
            result[i] = "  {}".format(result[i])
    result = "\n".join(result)
    return result


def talk2tex(template, item, last_timeslot):
    return template.render(command=commands.get(item["room"], default_cmd).get("command"), last_timeslot=last_timeslot, **item)


parser = argparse.ArgumentParser(description="convert Pretalx exports to LaTeX, output will be written to STDOUT")
parser.add_argument("-w", "--workshops", help="workshops only", action="store_true")
parser.add_argument("-d", "--day", help="day, format: YYYY-MM-DD")
parser.add_argument("template", help="template to render")
parser.add_argument("frab_export", help="Frab-compatible JSON export of Pretalx", type=argparse.FileType("r"))
args = parser.parse_args()

# read JSON
schedule = json.load(args.frab_export)["schedule"]
talks = []
for day in schedule["conference"]["days"]:
    if args.day and day["date"] != args.day:
        continue
    for room, sessions in day["rooms"].items():
        for talk in sessions:
            if args.workshops and talk["type"] != "Workshop":
                continue
            elif not args.workshops and talk["type"] == "Workshop":
                continue
            speakers = []
            for person in talk["persons"]:
                speakers.append(person["public_name"])
            speakers = ", ".join(speakers)
            abstract = break_long_lines(html.unescape(talk["abstract"]))
            talks.append({
                "date": datetime.datetime.strptime(talk["date"], DATE_FORMAT),
                "title": talk["title"],
                "room": talk["room"],
                "abstract": abstract,
                "speakers": speakers,
                "slug": talk["slug"],
                "type": talk["type"]
            })

# sort talks by start, then by room
talks.sort(key=lambda t : (t["date"], t["room"]))

# load template
template_dir = os.path.abspath(os.path.dirname(args.template))
jinja2_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    block_start_string='((%',
    block_end_string='%))',
    variable_start_string='(((',
    variable_end_string=')))',
    comment_start_string='((#',
    comment_end_string='#))',
    undefined=jinja2.StrictUndefined
)
jinja2_env.filters["e"] = escape_latex
jinja2_env.filters["datetimeformat"] = datetimeformat
template = jinja2_env.get_template(os.path.basename(args.template))

# render talks as LaTeX and write to file
last_timeslot = ""
for t in talks:
    out = talk2tex(template, t, last_timeslot)
    sys.stdout.write(out)
    last_timeslot = t["date"]
