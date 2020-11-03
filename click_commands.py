import click
import sys
import time
import check_web

# Open a file for save the Url's of the sites
f = open('websites.txt', 'a')
f.close()


# def the group of the cmd commands
@click.group()
def checker():
    click.echo("use q or ctrl+c for exit")
    pass


# Quit command
@checker.command(name="q")
def quit():
    click.echo("quiting the progress")
    sys.exit()


# print the list of Url's
@checker.command(name="print")
def print():
    f = open('websites.txt', 'r+')
    a = f.readlines()
    for line in a:
        click.echo(line)
    click.echo("that all")


# add a url to the list
@checker.command(name="add")
@click.argument('website', type=str)
def add(website):
    click.echo("adding the website")
    f = open('websites.txt', 'a')
    f.write(website)
    f.write('\n')


# delete url from the list
@checker.command(name="dlt")
@click.argument('website', type=str)
def delete(website):
    click.echo("deleting the progress")
    f = open('websites.txt', 'r+')
    a = f.readlines()
    f.seek(0)
    for line in a:
        if website not in line:
            f.write(line)
    f.truncate()
    f.close()


# start checking command
@checker.command(name="run")
@click.argument('times', default=-1, type=int)
def run(times=-1):
    click.echo("starting progress")
    if times == -1:  # if the user didn't give num of time he want to check
        while True:
            try:
                f = open('websites.txt', 'r+')
                a = f.readlines()
                for line in a:
                    if check_web.check_url(line):
                        click.echo(line + " is up")
                    else:
                        click.echo(line + " is down")
                f.close()
                time.sleep(10)
            except KeyboardInterrupt:
                print("\nexit progress")
                raise SystemExit
    else:
        for i in range(times):
            f = open('websites.txt', 'r+')
            a = f.readlines()
            for line in a:
                if check_web.check_url(line):
                    click.echo(line + " is up")
                else:
                    click.echo(line + " is down")
            f.close()
            if i != times - 1:
                time.sleep(10)
    click.echo("progress end")


if __name__ == '__main__':
    checker()
