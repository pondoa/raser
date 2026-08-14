"""Runtime construction shared by Signal entry points."""

from raser.core.current import cal_current as current
from raser.core.interaction.toy_mip import ToyMIPInteraction


def build_interaction(detector, seed, g4_vis, **options):
    if detector.g4_config.get("source_kind") == "toy_mip":
        return ToyMIPInteraction(detector, detector.g4_config, seed)

    from raser.core.interaction.interaction import GeneralG4Interaction

    return GeneralG4Interaction(
        detector,
        detector.g4_config,
        seed,
        g4_vis,
        **options,
    )


def is_toy_mip_source(interaction):
    return getattr(interaction, "geant4_model", None) == "toy_mip"


def build_current(detector, field, interaction, batch, *, keep_drift_paths=True):
    if is_toy_mip_source(interaction):
        return current.CalCurrentToyMIP(
            detector,
            field,
            interaction.source(batch),
            keep_drift_paths=keep_drift_paths,
        )
    return current.CalCurrentG4P(
        detector,
        field,
        interaction,
        batch,
        keep_drift_paths=keep_drift_paths,
    )
