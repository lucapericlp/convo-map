# convo-map

## Requirements
### Memory
#### LLM
Phi2

#### ASR
##### Whisper

Large
- (1550*1e06 * 4)/1024/1024/1024 = 5.77Gb @ fp32, 2.89Gb @ fp16
- 631s for 990s of audio


## Purpose

Real-time topic tracking to map out the landscape of a conversation

## Usage

- Upload an audio file
- Record from system audio
- Record from microphone

## Logic

Audio bytestream -> Audio file -> Text file -> Chart

## Rough notes
Implementation order in the spirit of "demo for yourself often":

1. **MapOut**: Given a diarised (only if it comes for free) transcription of a conversation,
   can we sample at some interval the entire conversation & incrementally build
   up an entity graph?
    - Implementation detail, stream from file as though it's continuously being
      appended so that the next "interface" steps is a breeze to implement -> maybe premature
      optimisation in action?
2. **StreamedTranscription**: Given an audio file, transcribe via Whisper & pass to the above functionality
3. **StreamedFromSource**: From microphone or from system audio, stream to audio
   file.
