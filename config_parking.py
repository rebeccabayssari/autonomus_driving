import pickle

parking_config = {
    "observation": {
        "type": "KinematicsGoal",  # Observation basée sur la cinématique avec objectif
        "features": ['x', 'y', 'vx', 'vy', 'cos_h', 'sin_h'],
        "scales": [100, 100, 5, 5, 1, 1],
        "normalize": False
    },
    "action": {
        "type": "ContinuousAction"  # Contrôle continu : accélération et direction
    },
    "duration": 30,  # Durée de l’épisode augmentée pour permettre le stationnement
    "simulation_frequency": 15,
    "policy_frequency": 5,
    "screen_width": 600,
    "screen_height": 300,
    "centering_position": [0.5, 0.5],
    "scaling": 7,
    "show_trajectories": True,  # Affichage des trajectoires pour mieux visualiser
    "render_agent": True,
    "offscreen_rendering": False,

    # Paramètres supplémentaires pertinents pour le parking
    "controlled_vehicles": 1,  # Un seul véhicule contrôlé
    "goal_reward": 1.0,        # Récompense pour atteinte du but
    "collision_penalty": -1.0, # Pénalité en cas de collision
    "parking_success_threshold": 0.5,  # Tolérance d’erreur de position/orientation pour réussir
    "angle_reward": True,      # Activer une récompense basée sur l’orientation
    "distance_reward": True,   # Activer une récompense basée sur la distance à la cible
}

with open("config_parking.pkl", "wb") as f:
    pickle.dump(parking_config, f)