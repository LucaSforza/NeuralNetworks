<script lang="ts">
  import type { Module } from "$lib/model/module";
  import { ENode } from "$lib/model/node";
  import { Handle, Position, type NodeProps } from "@xyflow/svelte";

  let { id, data, selected }: NodeProps = $props();

  let l: Module = $derived(ENode.fromId(data.enode as string)) as Module;

  function handleInternalClick() {
    console.log(`ActivationFunction ${id} was clicked!`);
  }

  function handleKeyDown(event: KeyboardEvent) {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      handleInternalClick();
    }
  }
</script>

<div
  class="activation-node"
  class:selected
  onclick={handleInternalClick}
  onkeydown={handleKeyDown}
  role="button"
  tabindex="0"
>
  <Handle type="target" position={Position.Top} />

  <div class="activation-label">
    {l.name}
  </div>

  <Handle type="source" position={Position.Bottom} />
</div>

<style>
  @import "../styles/activationFunction.css";
</style>
