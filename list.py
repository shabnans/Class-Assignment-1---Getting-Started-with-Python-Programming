{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "list.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPQ2vCtN/7rem57aJ8wTssw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shabnans/Class-Assignment-1---Getting-Started-with-Python-Programming/blob/master/list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VMSpv7dSm5kd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "list=[1,2,3,4,5,6]\n",
        "print(list)\n",
        "n=int(input(\"enter the search element:\"))\n",
        "for i in list:\n",
        "  if i==n:\n",
        "   print(\"search element is found\")\n",
        "   break\n",
        "else:\n",
        "   print(\"search element is not found\")"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}